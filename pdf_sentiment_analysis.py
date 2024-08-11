import PyPDF2 as Pdf
import pandas as pd
import nltk
import openpyxl
import requests
from io import BytesIO
import tkinter as tk
from tkinter import messagebox

#nltk.download("punkt") run this first time only
from nltk.tokenize import sent_tokenize
#nltk.download("vader_lexicon") run this first time only
from nltk.sentiment.vader import SentimentIntensityAnalyzer as Sia


def extract_text_from_pdf(url):
    text = ''
    try:
        response = requests.get(url)
    except:
        messagebox.showerror("File Error", "Invalid URL, Please try again")
        return None
    pdf_data = BytesIO(response.content)
    try:
        pdf_reader = Pdf.PdfFileReader(pdf_data)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
        return text
    except:
        messagebox.showerror("Unexpected Error", "An unexpected error occurred, Please try again")
        return None


def tokenizer(text):
    sentences = sent_tokenize(text)
    return sentences


def perform_sentiment_analysis(text, sentiment_model):
    sentences = tokenizer(text)
    neg_score = 0.0
    neu_score = 0.0
    pos_score = 0.0
    comp_score = 0.0
    count = 0.0
    for sentence in sentences:
        sentence_sentiment = sentiment_model.polarity_scores(sentence)
        neg_score += sentence_sentiment['neg']
        neu_score += sentence_sentiment['neu']
        pos_score += sentence_sentiment['pos']
        comp_score += sentence_sentiment['compound']
        count += 1
    sentiment_result = {
        'neg': neg_score/count,
        'neu': neu_score/count,
        'pos': pos_score/count,
        'compound': comp_score/count
    }
    return sentiment_result


def overall_sentiment(sentiment_result):
    if sentiment_result['compound'] > 0:
        overall_sent = 'POSITIVE'
    else:
        overall_sent = 'NEGATIVE'
    sentiment_result.update({'overall sentiment': overall_sent})

    return sentiment_result


def store_results_in_excel(sentiment_list, excel_path):
    df_new = pd.DataFrame(sentiment_list)
    columns_list = ['Negative Score', 'Neutral Score', 'Positive Score', 'Overall Score', 'Overall Sentiment', 'PDF URL']
    df_new.columns = columns_list
    with pd.ExcelFile(excel_path) as file:
        df_existing = pd.read_excel(file, sheet_name='Sheet1')
    updated_df = pd.concat([df_existing, df_new], ignore_index=True)
    with pd.ExcelWriter(excel_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        updated_df.to_excel(writer, sheet_name="Sheet1", index=False)


#Backend Main function
def backend_main():
    global sentiment_model
    global url
    global excel_path
    sentiment_button.config(text="Processing...", state="disabled", bg="grey")
    root.update_idletasks()
    if (excel_path is None) or (excel_path[-5:] != ".xlsx"):
        messagebox.showerror("File Not Found", "Error! Please enter the correct file name")
        excel_entry.delete(0, tk.END)
        sentiment_button.config(text="Perform Sentiment Analysis", state="normal", bg="#f57c00")
        return
    sentiment_list = []
    text = extract_text_from_pdf(url)
    if text is None:
        pdf_entry.delete(0, tk.END)
        sentiment_button.config(text="Perform Sentiment Analysis", state="normal", bg="#f57c00")
        return
    sentiment_result = perform_sentiment_analysis(text, sentiment_model)
    sentiment_result = overall_sentiment(sentiment_result)
    sentiment_result.update({"PDF URL": url})
    sentiment_list.append(sentiment_result)
    print(sentiment_result)
    messagebox.showinfo("PDF Analysed", f"Sentiment analysis saved to {excel_path}")
    store_results_in_excel(sentiment_list, excel_path)
    pdf_entry.delete(0, tk.END)
    sentiment_button.config(text="Perform Sentiment Analysis", state="normal", bg="#f57c00")


def on_click_pdf():
    global pdf_entry
    global url
    user_input = pdf_entry.get()
    if user_input == "":
        messagebox.showerror("Validation Error", "Please enter the PDF URL")
        return
    options = {
        'title': "Confirmation",
        'message': "Do you want to proceed with this URL?"
    }
    response = messagebox.askyesno(**options)
    if response:
        url = user_input

def on_click_excel():
    global excel_entry
    global excel_path
    user_input = excel_entry.get()
    if user_input == "":
        messagebox.showerror("File Error", "Please enter a correct filename")
        return
    options = {
        'title': "Confirmation",
        'message': f"Are you sure you want to save to this file: {user_input}"
    }
    response = messagebox.askyesno(**options)
    if response:
        excel_path = user_input


#define global variables: sentiment model, pdf url, and excel file
sentiment_model = Sia()
url = None
excel_path = None



root = tk.Tk()
root.title("Sentiment Analysis App")
root.geometry("600x400")

title_label = tk.Label(root, text="PDF Sentiment Analyzer", bg="#4CAF50", fg="white", font=("Helvetica", 16, "bold"))
title_label.pack(side=tk.TOP, fill=tk.X, pady=5, ipadx=10, ipady=10)

labelframe = tk.LabelFrame(root, text="INPUT", bg="#e0f7fa", font=("Helvetica", 12, "bold"))
labelframe.pack(pady=5, fill=tk.BOTH, expand=True)

pdf_label = tk.Label(labelframe, text='Enter PDF URL', bg="#e0f7fa")
pdf_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

pdf_entry = tk.Entry(labelframe)
pdf_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

pdf_button = tk.Button(labelframe, text='Enter', command=on_click_pdf, bg="#4CAF50", fg="white")
pdf_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

excel_label = tk.Label(labelframe, text="Enter the Excel File name", bg="#e0f7fa")
excel_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

excel_entry = tk.Entry(labelframe)
excel_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

excel_button = tk.Button(labelframe, text="Enter", command=on_click_excel, bg="#4CAF50", fg="white")
excel_button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

sentiment_button = tk.Button(root, text="Perform Sentiment Analysis",bg='#f57c00', fg="white", command=backend_main, state="normal", font=("Helvetica", 14, "bold"))
sentiment_button.pack(side=tk.BOTTOM, ipadx=30, ipady=30, fill=tk.X)

root.mainloop()




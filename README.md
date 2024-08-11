# URL-Sentiment-Analysis
The PDF Sentiment Analyzer is a Python-based application that allows users to perform sentiment analysis on text extracted from PDF files. This tool utilizes various Python libraries such as nltk for sentiment analysis, PyPDF2 for PDF text extraction, pandas for data handling, and tkinter for creating a simple graphical user interface (GUI).

Users can input a PDF URL and specify an Excel file to store the analysis results. The application extracts the text from the PDF, performs sentiment analysis on the text, and saves the results in the specified Excel file. The tool provides feedback and error handling through popup messages.

# Features
- Extracts text from a PDF file using a provided URL.
- Tokenizes the extracted text into sentences.
- Performs sentiment analysis using the VADER sentiment analysis tool from the nltk library.
- Stores the sentiment analysis results in an Excel file.
- Provides a simple GUI for user interaction.
- Handles errors and provides feedback using tkinter message boxes.

# Requirements
The python version and other packages are listed in "REQUIREMENTS.TXT" file

# How to Use
1. PDF URL Input: Enter the URL of the PDF file you want to analyze.
2. Excel File Name Input: Enter the name of the Excel file where you want to store the analysis results.
3. Perform Sentiment Analysis Button: Starts the sentiment analysis process.

# Code Explanation
I defined functions for each of the different tasks such as extracting data from PDFs, processing the text and performing sentiment analysis, writing the result to excel file, etc. Then, I defined the 'backend_main' which calls each of the individual functions in sequential order. Details for each function is given bellow:
'extract_text_from_pdf(url)': Downloads the PDF file from the provided URL and extracts the text.
'tokenizer(text)': Tokenizes the extracted text into sentences using 'nltk.sent_tokenize'.
'perform_sentiment_analysis(text, model)': Performs sentiment analysis on each sentence using VADER and returns an aggregated sentiment score across all sentences.
'overall_sentiment(sentiment_result)': Determines the overall sentiment (positive or negative) based on the compound score.
'store_results_in_excel(sentiment_list, excel_path)': Stores the sentiment analysis results in an Excel file.

The GUI has a top label, a label frame which includes buttons and entry widgets for entering the URL and excel file name, and a button in the bottom to start the back-end process. 
# Final Result

GUI Interface:

![image](https://github.com/user-attachments/assets/194b3050-c226-4687-a8d9-be4d63543b71)

Error Handling message:

![image](https://github.com/user-attachments/assets/02b071ef-b968-41b6-a51e-3ee004e1fd5b)

Process Complete:

![image](https://github.com/user-attachments/assets/44f047f9-99e8-427d-b606-826c7a30a1c1)

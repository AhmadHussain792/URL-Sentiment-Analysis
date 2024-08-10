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


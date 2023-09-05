import nltk
import openai
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import requests
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import streamlit as st

from nltk.tokenize import word_tokenize
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient

nltk.download('punkt')
# Set your OpenAI API key
openai.api_key = st.secrets["YOUR_API_KEY"]

# Function to generate chatbot response using OpenAI
def amz_chatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=100, 
        temperature=0.7  
    )
    return response['choices'][0]['text'].strip()

def main():
    st.write("Welcome to the Product Reviewing Chatbot!")
    st.write("For exiting the chatbot type 'exit'")

    while True:
        user_input = st.text_input("You:", "")

        if user_input.lower() == 'exit':
            st.write("Chatbot: Bye!")
            break

        prompt = f"You: {user_input}\nChatbot:"
        chatbot_response = amz_chatbot(prompt)

        st.write(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()

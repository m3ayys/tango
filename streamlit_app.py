
import streamlit as st
import random

# Define the quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]

# Define the sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fortune"])

# Define the pages
if page == "Home":
    st.title("Famous American Quotes")
    st.write("Welcome to the Famous American Quotes app! Click on 'Fortune' in the sidebar to get your daily quote.")
elif page == "Fortune":
    st.title("Your Daily Fortune")
    st.write("Click the button below to get your daily quote.")
    if st.button("Get Quote"):
        quote = random.choice(quotes)
        st.write(quote)
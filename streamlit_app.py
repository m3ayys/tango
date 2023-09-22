
import streamlit as st
import random

# Define the quotes and their vocabulary words
quotes = {
    "Abraham Lincoln": {
        "quote": "Nearly all men can stand adversity, but if you want to test a man's character, give him power.",
        "vocab": ["adversity", "character"]
    },
    "Martin Luther King Jr.": {
        "quote": "The time is always right to do what is right.",
        "vocab": ["time", "right"]
    },
    "Eleanor Roosevelt": {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "vocab": ["future", "beauty", "dreams"]
    }
}

# Define the quiz function
def quiz():
    # Select a random quote
    author, quote = random.choice(list(quotes.items()))
    # Select a random vocabulary word
    vocab_word = random.choice(quote["vocab"])
    # Ask the user to provide the definition
    definition = st.text_input(f"What is the definition of '{vocab_word}' in this quote by {author}?\n\n{quote['quote']}")
    # Check the answer
    if definition.lower() == vocab_word.lower():
        st.write("Correct!")
    else:
        st.write(f"Sorry, the correct answer was '{vocab_word}'.")

# Define the sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Quiz"])

# Define the pages
if page == "Home":
    st.title("Famous American Quotes")
    for author, quote in quotes.items():
        st.write(f"**{author}:** {quote['quote']}")
elif page == "Quiz":
    st.title("Vocabulary Quiz")
    quiz()
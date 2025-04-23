import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sqlite3
import datetime

# Load API key from .env file
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("API_KEY")  # Retrieve API key securely
if not api_key:
    raise ValueError("API key not found. Please set it in the .env file.")

genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Set up SQLite database for persistent chat history
conn = sqlite3.connect("chat_history.db")
cursor = conn.cursor()

# Ensure table structure is correct
cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        message TEXT
    )
""")
conn.commit()

# Function to save chat history
def save_chat(category, message):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO chats (date, category, message) VALUES (?, ?, ?)", (date, category, message))
    conn.commit()

# Function to load chat history
def load_chat(category=None, date=None):
    if category and date:
        cursor.execute("SELECT message FROM chats WHERE category=? AND date=? ORDER BY id", (category, date))
    elif category:
        cursor.execute("SELECT message FROM chats WHERE category=? ORDER BY id", (category,))
    else:
        cursor.execute("SELECT message FROM chats ORDER BY id")
    return [row[0] for row in cursor.fetchall()]

# Streamlit UI
st.title("🎓 Studybot AI Chat Page")

# Select Category
category = st.sidebar.selectbox(
    "Select a Category:",
    ["📧 Email Drafting", "📚 Academic Help", "💻 Coding Help", "📄 Assignment Assistance"]
)

# Chat History Management
chat_date = st.date_input("📅 Select Date to View Previous Chats")
if st.button("Load Previous Chats"):
    history = load_chat(category, chat_date.strftime("%Y-%m-%d"))
    if history:
        st.write(f"📜 **Previous Conversations in {category} on {chat_date}:**")
        for msg in history:
            st.write(msg)
    else:
        st.write("No past conversations found for this date and category.")

# Start a New Chat
st.subheader(f"💬 Chat with Studybot AI in {category}")
user_input = st.text_area("Type your message:")

if st.button("Submit"):
    chat_prompt = f"{category}: {user_input}"
    try:
        chat_response = model.generate_content(chat_prompt)

        if chat_response and chat_response.text:
            chat_reply = f"🤖 **AI Response:** {chat_response.text}"
            save_chat(category, chat_reply)
            st.write(chat_reply)
        else:
            st.write("I couldn't generate a response, please try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Close SQLite connection when the app is stopped
conn.close()

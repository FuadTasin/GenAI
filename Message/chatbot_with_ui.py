from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
import streamlit as st

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

st.header("ChatBot")

user_input=st.chat_input("Type your message")

if user_input:
    if user_input.strip().lower()=="exit":
        st.stop()
    with st.chat_message('human'):
        st.write(user_input)

    result=model.invoke(user_input)

    with st.chat_message('assistant'):
        st.write(result.content)
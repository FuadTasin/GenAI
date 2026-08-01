from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

model=ChatGroq(
    model="openai/gpt-oss-120b"
)

st.header("Research Tool")

user_input=st.text_input("Enter Your Prompt")

if st.button("Summirize"):
    result=model.invoke(user_input)

    st.write(result.content)

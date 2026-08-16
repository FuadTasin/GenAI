from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

st.header("ChatBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

with st.sidebar:
    st.subheader("Chat History")

    if not st.session_state.chat_history:
        st.write("Empty")
    else:
        for msg in st.session_state.chat_history:
            role='AI' if isinstance(msg,AIMessage) else 'Human'
            st.write(f"{role}:{msg.content}")

for msg in st.session_state.chat_history:
    role='assistant' if isinstance(msg,AIMessage) else 'human'

    with st.chat_message(role):
        st.write(msg.content)

user_input=st.chat_input("Enter Your Message:")

if user_input:

    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message('human'):
        st.write(user_input)
    
    result=model.invoke(st.session_state.chat_history)

    with st.chat_message('assistant'):
        st.write(result.content)
    
    st.session_state.chat_history.append(
        AIMessage(content=result.content)
    )
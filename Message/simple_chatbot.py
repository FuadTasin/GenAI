from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import HumanMessage,AIMessage,SystemMessage

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

chat_history=[SystemMessage(content="You are a helpful assistant.Always ans in a short paragraph(1-2 sentence)")]

while True:
    user_input=input("You  :")

    chat_history.append(HumanMessage(content=user_input))

    ai_output=model.invoke(chat_history)

    chat_history.append(AIMessage(content=ai_output.content))

    print("AI  :",ai_output.content)

    cont=input("Do you want to continue(Yes/No)? --->")
    if (cont.lower())=="yes":continue
    elif(cont.lower()=="no"): break

print(chat_history)
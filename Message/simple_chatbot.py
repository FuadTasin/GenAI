from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

while True:
    user_input=input("You  :")

    ai_output=model.invoke(user_input)

    print("AI  :",ai_output.content)

    cont=input("Do you want to continue(Yes/No)? --->")
    if (cont.lower())=="yes":continue
    elif(cont.lower()=="no"): break
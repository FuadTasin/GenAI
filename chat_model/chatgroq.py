from langchain_groq import ChatGroq
from dotenv import load_dotenv

load=load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-120b"
)

result=llm.invoke("Tell me what is ai?")
print(result.content)
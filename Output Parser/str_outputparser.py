from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.3)

prompt=PromptTemplate.from_template(
    "Explain {topic} in simple term"
)

parser=StrOutputParser()

chain=prompt|model|parser

result=chain.invoke({
    "topic":"Machine Learning"
})

print(result)
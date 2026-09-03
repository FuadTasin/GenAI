from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader=PyPDFLoader('Advances_in_Machine_Learning_Algorithms_for_Hate_Speech_Detection_in_Social_Media_A_Review.pdf')
docs=loader.load()

# print(len(docs))
# print(type(docs))
# print(docs[1])
# print(docs[0].page_content)
# print(docs[1].metadata)

model=ChatGroq(model='openai/gpt-oss-120b',temperature=0.5)
parser=StrOutputParser()
prompt=PromptTemplate(
    template="""
    Write a summary of the following text(should be in 5-10 sentences):
    {text}
    """,
    input_variables=["text"]
)

chain=prompt|model|parser

result=chain.invoke({
    "text":docs[1]
})
print(result)
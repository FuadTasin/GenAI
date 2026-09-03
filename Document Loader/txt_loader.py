from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader=TextLoader('poem.txt',encoding='utf-8')

docs=loader.load()

# print(docs)
# print(type(docs))  -> multiple list of document
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

model=ChatGroq(model='openai/gpt-oss-120b',temperature=0.5)
parser=StrOutputParser()
prompt=PromptTemplate(
    template="""
    Write a summary of the following poem:
    {poem}
    """,
    input_variables=["poem"]
)

chain=prompt|model|parser

result=chain.invoke({
    "poem":docs[0].page_content
})
print(result)

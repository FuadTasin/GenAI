from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader=DirectoryLoader(
    path='.',
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# docs=loader.load()
# print(len(docs))
# print(docs[26].page_content)

docs=loader.lazy_load()

for document in docs:
    print(document.metadata)


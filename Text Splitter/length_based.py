from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader=PyPDFLoader('Advances_in_Machine_Learning_Algorithms_for_Hate_Speech_Detection_in_Social_Media_A_Review.pdf')

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

result=splitter.split_documents(docs)
print(len(result))
print(result[0].page_content)
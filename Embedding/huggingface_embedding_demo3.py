from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

vector=embeddings.embed_documents(
    [
    "Who is spiderman",
    "tell me about pokemon",
    "Tell a funny story"
]
)

print(vector[0])
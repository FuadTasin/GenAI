from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

vectors=embeddings.embed_documents([
    "Who is spiderman",
    "tell me about pokemon",
    "Tell a funny story"
])

print(len(vectors),vectors[0])
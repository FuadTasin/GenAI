from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

documents=[
    "I love programming in python.It is my favourite language",
    "JavaScript is great for buildings web applications",
    "Eating pizza with friends in a friday night",
    "Python is awsome for data science and machine learning",
    "I enjoy hiking in the mountails during summer"
]

query="I like python."

doc_vector=embedding.embed_documents(documents)

query_vector=embedding.embed_query(query)

scores=cosine_similarity([query_vector],doc_vector)
# print(scores)

idx=np.argmax(scores)
# print(idx)
score=scores[idx]


print(scores[idx])

print("Query:",query)
print("Most Similar Document:",documents[idx])
print("Similarity Score",score)
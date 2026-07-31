from sentence_transformers import SentenceTransformer,util

model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)

s1="I love python programming"
s2="Python coding is my passion"
s3="I love to eat pizza"

em1=model.encode(s1)
em2=model.encode(s2)
em3=model.encode(s3)

print(util.cos_sim(em1,em2))
print(util.cos_sim(em1,em3))
print(util.cos_sim(em2,em3))


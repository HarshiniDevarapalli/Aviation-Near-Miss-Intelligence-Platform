from src.embedding_model import EmbeddingModel

model = EmbeddingModel()

embedding = model.encode_query(
    "Aircraft taxiing in low visibility."
)

print(type(embedding))
print(embedding.shape)
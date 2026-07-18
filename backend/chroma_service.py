import chromadb

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_or_create_collection(
    name="research_documents"
)


def store_embeddings(chunks, embeddings):

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings.tolist()
    )
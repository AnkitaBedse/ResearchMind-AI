import chromadb
import uuid
from embedding_service import embedding_model


client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_or_create_collection(
    name="research_documents"
)

def document_exists(file_hash):

    results = collection.get(
        where={"file_hash": file_hash}
    )

    return len(results["ids"]) > 0


def store_embeddings(chunks, embeddings, filename, file_hash):

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [
        {
            "filename": filename,
            "chunk_number": index + 1,
            "file_hash": file_hash
        }
        for index in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

def retrieve_relevant_chunks(query):

    query_embedding = embedding_model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )
    return {
    "documents": results["documents"][0],
    "metadata": results["metadatas"][0]
    }
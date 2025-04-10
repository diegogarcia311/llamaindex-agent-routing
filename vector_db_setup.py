from llama_index import VectorStoreIndex, SimpleDirectoryReader

def build_index(folder: str, index_name: str):
    docs = SimpleDirectoryReader(folder).load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.save_to_disk(index_name)

if __name__ == "__main__":
    build_index("data/travel_docs", "vector_travel")
    build_index("data/tech_docs", "vector_tech")
    build_index("data/general_docs", "vector_general")


from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llm_response_validator import validate_response

def classify_expense(expense_text: str, user_region: str = "US"):
    if "flight" in expense_text.lower() or "uber" in expense_text.lower():
        agent = VectorStoreIndex.load_from_disk("vector_travel")
        category = "Travel"
    elif "subscription" in expense_text.lower() or "software" in expense_text.lower():
        agent = VectorStoreIndex.load_from_disk("vector_tech")
        category = "Tech"
    else:
        agent = VectorStoreIndex.load_from_disk("vector_general")
        category = "General"

    query_engine = agent.as_query_engine()
    result = query_engine.query(f"Classify this: {expense_text}")

    if validate_response(result.response, expected_category=category):
        print(f"✓ Validated [{category}] Response:", result.response)
    else:
        print("⚠️ Response validation failed.")

if __name__ == "__main__":
    classify_expense("Slack subscription renewal")


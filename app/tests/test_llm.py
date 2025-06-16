from app.utils.llm import generate_answer

docs = [
    "RAG stands for Retrieval Augmented Generation, a technique that enhances LLMs.",
    "It works by retrieving relevant chunks from a document and passing them to the model.",
]

question = "What is RAG?"
response = generate_answer(question, docs)

print(f"\nAnswer:\n{response}")

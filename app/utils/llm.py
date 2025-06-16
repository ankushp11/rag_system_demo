from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer


model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
llm = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)


def generate_answer(
    query: str, retrieved_docs: list[str], chat_history: list[str] = []
) -> str:
    """
    Generate an answer using the query and retrieved documents.
    chat_history: optionally pass a list of previous Q&A turns
    """

    context = "\n".join([f"- {doc}" for doc in retrieved_docs])
    history = "\n".join([f"{h}" for h in chat_history])

    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Conversation History:
{history}

Question: {query}
Answer:"""

    output = llm(prompt, max_new_tokens=256, truncation=True)[0]["generated_text"]
    return output.split("Answer:")[-1].strip()

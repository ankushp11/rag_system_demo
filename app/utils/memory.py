conversation_history = []


def get_conversation_history():
    return conversation_history


def update_conversation_memory(question: str, answer: str):
    conversation_history.append((question, answer))

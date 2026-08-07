import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge_base.json"


def load_knowledge_base():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def search_knowledge(user_question):
    """Find relevant knowledge entries by matching keywords in the question."""
    kb = load_knowledge_base()
    question_lower = user_question.lower()
    matches = []
    for entry in kb:
        # if any keyword appears in the question, this entry is relevant
        if any(keyword in question_lower for keyword in entry["keywords"]):
            matches.append(entry["info"])
    return matches





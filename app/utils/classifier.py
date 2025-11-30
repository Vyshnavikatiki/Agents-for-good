def classify(query: str):
    q = query.lower()

    if any(w in q for w in ["climate", "pollution", "green", "plastic", "recycle"]):
        return "green"

    if any(w in q for w in ["health", "disease", "first aid", "injury", "symptom"]):
        return "health"

    if any(w in q for w in ["explain", "study", "learn", "teach", "exam"]):
        return "edu"

    if any(w in q for w in ["policy", "rights", "government", "civic", "law"]):
        return "civic"

    return "edu"

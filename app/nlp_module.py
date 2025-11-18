from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyse_document(texte):
    labels = [
        "erreur administrative",
        "violation du droit",
        "information incomplète",
        "aucun problème détecté"
    ]
    result = classifier(texte, candidate_labels=labels)
    return result["labels"][0]
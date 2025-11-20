from app.nlp_module import analyse_document


def test_analyse_document():
    texte = "J'ai reçu une amende qui contient une erreur administrative sur la date."
    label = analyse_document(texte)
    assert label in [
        'erreur administrative', 'violation du droit', 'information incomplète', 'aucun problème détecté
    ]

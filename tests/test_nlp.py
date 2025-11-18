from app.nlp_module import analyse_document

def test_analyse_document():
    texte = "L'avis d'amende comporte une erreur administrative évidente."
    assert analyse_document(texte) in [
        "erreur administrative",
        "violation du droit",
        "information incomplète"
    ]
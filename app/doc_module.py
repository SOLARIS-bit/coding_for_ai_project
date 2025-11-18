from docxtpl import DocxTemplate

def generate_recourse(probleme_detecte):
    doc = DocxTemplate("template_recours.docx")
    context = {
        "probleme": probleme_detecte,
        "explication": (
            "Votre dossier semble contenir une " + probleme_detecte +
            ", ce qui peut justifier un recours administratif."
        )
    }
    output_path = "recours_genere.docx"
    doc.render(context)
    doc.save(output_path)
    return output_path
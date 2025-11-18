from flask import Flask, request, render_template, send_file
from nlp_module import analyse_document
from doc_module import generate_recourse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["document"]
        texte = file.read().decode("utf-8", errors="ignore")
        result = analyse_document(texte)
        output_path = generate_recourse(result)
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
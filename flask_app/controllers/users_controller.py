
from flask import render_template, redirect, request, session
from flask_app import app
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def checker_clone(student_notes, student_files):

    def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
    def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

    vectors = vectorize(student_notes)
    s_vectors = list(zip(student_files, vectors))
    plagiarism_results = set()

    def check_plagiarism(s_vectors1):
        s_vectors=s_vectors1
        for student_a, text_vector_a in s_vectors:
            new_vectors = s_vectors.copy()
            current_index = new_vectors.index((student_a, text_vector_a))
            del new_vectors[current_index]
            for student_b, text_vector_b in new_vectors:
                sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                student_pair = sorted((student_a, student_b))
                score = (student_pair[0], student_pair[1], sim_score*100)
                plagiarism_results.add(score)
        return plagiarism_results

    for data in check_plagiarism(s_vectors):
        return data


@app.route("/")
def index():
    if "texto1" in session:
        texto1 = session["texto1"]
    else:
        texto1='nada'

    if "texto2" in session:
        texto2 = session["texto2"]
    else:
        texto2='nada'
    print(texto1)
    print(texto2)
    student_notes=[texto1,texto2]

    # ====================================
    student_files=["texto 1", "texto 2"]
    
    data = checker_clone(student_notes, student_files)
    porcent = "{0:.2f}".format(data[2])
    print(data)
    print(data[2])

    # ====================================

    return render_template("dashboard.html", texto1=texto1, texto2=texto2, porcent=porcent)


@app.route("/plagiarism-checker", methods=["POST"])
def check_plagiarism():
    print(request.form)
    texto1 = request.form["text1"]
    texto2= request.form["text2"]
    session["texto1"] = texto1
    session["texto2"]= texto2

    return redirect("/")



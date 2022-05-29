
from flask import render_template, redirect, request, session
from flask_app import app

@app.route("/")
def index():
    if "texto1" in session:
        texto1 = session["texto1"]
    else:
        texto1=''

    if "texto2" in session:
        texto2 = session["texto2"]
    else:
        texto2=''

    
    return render_template("dashboard.html", texto1=texto1, texto2=texto2)


@app.route("/plagiarism-checker", methods=["POST"])
def check_plagiarism():
    print(request.form)
    texto1 = request.form["text1"]
    texto2= request.form["text2"]
    session["texto1"] = texto1
    session["texto2"]= texto2

    return redirect("/")



from flask import render_template, redirect, request, get_flashed_messages
from flask_app import app

@app.route("/")
def index():
    return render_template("dashboard.html")


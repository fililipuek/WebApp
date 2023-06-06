from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.jinja")

@app.route("/book/<id>")
def book(id):
    return render_template("book.jinja", id = id)

@app.route("/about")
def about():
    return render_template("about.jinja")
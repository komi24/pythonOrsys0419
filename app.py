# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from models import db
from models.users import User
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ge.sqlite3"

with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route('/')
def hello():
    liste = User.query.all()
    return render_template("index.html", liste=liste)


@app.route('/profile/<id>')
def profile(id):
    # Autre possibilité
    # liste = User.query.filter_by(id = id)
    liste = User.query.filter(User.id == id)
    return render_template(
            "index.html", 
            liste=liste, 
            userid=id)

@app.route('/update/<id>', methods=["POST","GET"])
def update(id):
    # Autre possibilité
    # liste = User.query.filter_by(id = id)
    if request.method == "GET":
        user = User.query.filter(User.id == id).first()
        return render_template(
                "update.html", 
                user=user)
    
    User.query.filter(User.id == id).update({
            "nom": request.form.get("nom"),
            "email": request.form.get("email")
            })
    db.session.commit()
    return redirect("/")

@app.route('/mon_form', methods=["POST"])
def form():
    mail = request.form.get("email")
    nom = request.form.get("nom")
    pwd = request.form.get("pwd")
    personne = User(nom, mail, pwd)
    db.session.add(personne)
    db.session.commit()
    return render_template(
            "index.html", 
            message=mail,
            nom=nom
            )


app.run(debug=True, port=8080)
# -*- coding: utf-8 -*-

from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    def __init__(self, nom, email, password):
        self.nom = nom
        self.email = email
        self.password = password
        
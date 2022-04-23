from . import db

class Names(db.Model):
    # Datebase Columns #
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    age = db.Column(db.Integer, nullable = False)
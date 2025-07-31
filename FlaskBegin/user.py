from helper.extensions import db

class User(db.Model):
    user_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    password =  db.Column(db.String(100))
    gmail = db.Column(db.String(100))
    def __init__(self, name: str = "NULL", password: str = "NULL", gmail: str = "NULL"):
        self.name = name
        self.password = password
        self.gmail = gmail
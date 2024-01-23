from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    surname = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(32), unique = True, nullable = False)

    def __repr__(self):
        return f'User({self.name}, {self.surname}, {self.email}, {self.password})'



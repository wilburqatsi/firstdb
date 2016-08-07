from tableask import db, app


class Table(db.Model):

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    Tnumber= db.Column(db.Integer)

class Laptop(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    maker = db.Column(db.String(50))
    color = db.Column(db.String(50))

class Dishware(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cup = db.Column(db.String(50))
    glass = db.Column(db.String(50))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numpage = db.Column(db.Integer)

db.create_all(app=app)
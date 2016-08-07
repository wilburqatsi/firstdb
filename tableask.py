from flask import Flask, render_template, request
import flask_sqlalchemy

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = flask_sqlalchemy.SQLAlchemy(app)

from models import Laptop
#import models

@app.route('/')
def entityinput():
    return render_template('inputpage.html')

@app.route('/pagesubmitted/', methods=['post'])
def pagesubmit():
    print("inside pageSubmit")

    tableNum = request.form['tableNum']
    maker = request.form['maker']
    color = request.form['color']
    purpose = request.form['purpose']
    pagenum = request.form['pagenum']
    print("data collected")

    print(tableNum, maker, color, purpose, pagenum)

    laptop = Laptop()

    laptop.maker = maker
    laptop.color = color

    db.session.add(laptop)
    db.session.commit()

    return render_template('pagesubmit.html', tablenum = tableNum, maker = maker, color = color, purpose = purpose, pagenum = pagenum)


app.run()
#from flask import Flask, render_template, request
#import flask_sqlalchemy

#app = Flask(__name__)
#app.config.from_pyfile('settings.py')
#db = flask_sqlalchemy.SQLAlchemy(app)

#import models

#@app.route('/')
#def index():
#    return render_template("form.html")


#@app.route('/getLogin', methods=['post'])
#def login():
#    user_name = request.form['uname']
#    password = request.form['passw']
#    print(user_name)
#    print(password)

#    return render_template('testie.html', uname = user_name, passw = password)

#def testie():

#    return render_template('testie.html')


#app.run()
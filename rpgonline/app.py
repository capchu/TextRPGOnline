# all the imports
import os
import sqlite3
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.mail import Mail, Message
from dataAccess import DataAccess

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)
login_code = {}

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/index')
#def index():
#    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/character_edit')
def character_edit():
    DA = DataAccess()
    abilities = DA.getAbilities().all()
    weaknesses = DA.getWeaknesses().all()
    perks = DA.getPerks().all()
    flaws = DA.getFlaws().all()
    return render_template('character_edit.html', abilities=abilities, weaknesses=weaknesses,
                           perks=perks, flaws=flaws)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
	return render_template('index.html')

    email1 = None
    email2 = None
    if request.method == 'POST':
	if 'Code' in request.form:
	    email = request.form['Email']
	    log_code = request.form['Code']

	    print "Check"
	    print login_code
	    if email not in login_code:
		email2 = "Invalid E-mail and Code combination"
		return render_template('login.html', email1=email1, email2=email2)
	    if login_code[email] != log_code:
		email2 = "Invalid E-mail and Code combination"
		return render_template('login.html', email1=email1, email2=email2)

	    print "Login"
#	    session['username'] = email
	    del login_code[email]
	    return render_template('index.html')
	else:
	    email = request.form['Email']
	    if email.find('@') == -1:
		email1 = "%s is not a valid E-mail address" % email
		print email1
		return render_template('login.html', email1=email1, email2=email2)

	    login_code[email] = get_code()

	    msg = Message("Hello", 
				recipients=[email])
	    email1 = "Sending login code to %s" % email
#	    mail.send(msg)

	    return render_template('login.html', email1=email1, email2=email2)

    return render_template('login.html', email1=email1, email2=email2)

def get_code():
    return 'alkdjf'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

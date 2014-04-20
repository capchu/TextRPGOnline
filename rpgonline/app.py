# all the imports
import random
import os
import string
import sqlite3
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.mail import Mail, Message
from dataAccess import DataAccess
from databaseCreation import Character
from clientCharacter import ClientCharacter
from clientCharacter import ClientDataAccess

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
#mail = Mail(app)
login_code = {}

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
##app.config['MAIL_SERVER'] = 'smtp.gmail.com'
##app.config['MAIL_PORT'] = 465
##app.config['MAIL_USE_TLS'] = False
##app.config['MAIL_USE_SSL'] = True
##app.config['MAIL_USERNAME'] = 'ova.app.test@gmail.com'
##app.config['MAIL_PASSWORD'] = 'testovaapp'
##app.config['DEFAULT_MAIL_SENDER'] = 'ova.app.test@gmail.com'

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ova.app.test@gmail.com',
    MAIL_PASSWORD = 'testovaapp',
    MAIL_DEFAULT_SENDER = 'ova.app.test@gmail.com'
))

mail = Mail(app)
##
#
# Methods for html page requests
#
##
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/character_create')
def character_create():
    return render_template('character_create.html')

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
	session.pop('username', None)
	return render_template('index.html')

    email1 = None
    email2 = None
    if request.method == 'POST':
	if 'Code' in request.form:
	    email = request.form['Email']
	    log_code = request.form['Code']

	    print login_code
	    if email not in login_code:
		email2 = "Invalid E-mail and Code combination"
		return render_template('login.html', email1=email1, email2=email2)
	    if login_code[email] != log_code:
		email2 = "Invalid E-mail and Code combination"
		return render_template('login.html', email1=email1, email2=email2)

	    session['username'] = email
	    del login_code[email]
	    return render_template('index.html')
	else:
	    email = request.form['Email']
	    if email.find('@') == -1:
		email1 = "%s is not a valid E-mail address" % email
		print email1
		return render_template('login.html', email1=email1, email2=email2)

	    login_code[email] = get_code()

	    msg = Message("Login Code for RPG Online", 
				recipients=[email])
	    msg.body = "login code: %s" % login_code[email]
	    email1 = "Sending login code to %s" % email
	    mail.send(msg)

	    return render_template('login.html', email1=email1, email2=email2)

    return render_template('login.html', email1=email1, email2=email2)

def get_code():
    size = 10
    chars=string.ascii_letters + string.digits

    return ''.join(random.choice(chars) for _ in range(size))

##
#
# Methods for JSON requests
#
##
@app.route('/add_character_json')
def add_character_json():
    CDA = ClientDataAccess()
    #new_character = ClientCharacter()
    #CDA.addClientCharacter(new_character)
    
@app.route('/character_list_json')
def character_list_json():
    DA = DataAccess()
    characters_object = DA.getCharacters(request.args.get('name', 0, type=str))
    character_list = {}
    
    for char_obj in characters_object:
        character_list[char_obj.id] = {}
        character_list[char_obj.id]['user_id'] = char_obj.user_id
        character_list[char_obj.id]['name'] = char_obj.name
        character_list[char_obj.id]['combat_notes'] = char_obj.combat_notes
        character_list[char_obj.id]['defense'] = char_obj.defense
        character_list[char_obj.id]['health'] = char_obj.health
        character_list[char_obj.id]['endurance'] = char_obj.endurance
        character_list[char_obj.id]['tv'] = char_obj.tv
        character_list[char_obj.id]['background'] = char_obj.background
        character_list[char_obj.id]['appearance'] = char_obj.appearance
        character_list[char_obj.id]['personality'] = char_obj.personality
        character_list[char_obj.id]['other_notes'] = char_obj.other_notes
        character_list[char_obj.id]['portrait_url'] = char_obj.portrait_url
        character_list[char_obj.id]['icon_url'] = char_obj.icon_url
        
    return jsonify(character_list)

@app.route('/specific_character_json')
def specific_character_json():
    #DA = DataAccess()
    CDA = ClientDataAccess()
    character = CDA.getClientCharacter('1')#request.args.get('id', 0, type=int))
    character_info = {}
    
    character_info['user_id'] = character.user_id
    character_info['name'] = character.name
    character_info['combat_notes'] = character.combat_notes
    
    for a in character.abilities:
        character_info['ability_list'] = {}
        character_info['ability_list']['ability_id'] = a.ability_id
        character_info['ability_list']['ability_value'] = a.value
        character_info['ability_list']['ability_note'] = a.note
        
    for w in character.weaknesses:
        character_info['weakness_list'] = {}
        character_info['weakness_list']['weakness_id'] = w.weakness_id
        character_info['weakness_list']['weakness_value'] = w.value
        character_info['weakness_list']['weakness_note'] = w.note

    for a in character.attacks:
        character_info['attack_list'] = {}
        character_info['attack_list']['name'] = a.name
        
        for p in a.perks:
            character_info['attack_list']['perks'] = {}
            character_info['attack_list']['perks']['perk_id'] = p.perk_id
            character_info['attack_list']['perks']['multiplier'] = p.multiplier
            character_info['attack_list']['perks']['note'] = p.note
            
        for f in a.flaws:
            character_info['attack_list']['perks'] = {}
            character_info['attack_list']['perks']['perk_id'] = f.flaw_id
            character_info['attack_list']['perks']['multiplier'] = f.multiplier
            character_info['attack_list']['perks']['note'] = f.note
        
        character_info['attack_list']['roll'] = a.roll
        character_info['attack_list']['dx'] = a.dx
        character_info['attack_list']['end'] = a.end
        character_info['attack_list']['note'] = a.note
    
    character_info['defense'] = character.defense
    character_info['health'] = character.health
    character_info['endurance'] = character.endurance
    character_info['tv'] = character.tv
    character_info['background'] = character.background
    character_info['appearance'] = character.appearance
    character_info['personality'] = character.personality
    character_info['other_notes'] = character.other_notes
    character_info['portrait_url'] = character.portrait_url
    character_info['icon_url'] = character.icon_url
    
    print character_info
    return jsonify(character_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


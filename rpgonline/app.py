# all the imports
import os
import sqlite3
from flask import Flask, jsonify, request, session, g, redirect, url_for, abort, \
     render_template, flash
from dataAccess import DataAccess
from databaseCreation import Character
from clientCharacter import ClientCharacter
from clientCharacter import ClientDataAccess

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

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
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

##
#
# Methods for JSON requests
#
##
@app.rout('/add_character_json')
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
    character = CDA.getClientCharacter('1')#request.args.get('id', 0))
    character_info = {}
    
    character_info['user_id'] = character.user_id
    character_info['name'] = character.name
    character_info['combat_notes'] = character.combat_notes
    
    for a in character.ability_list:
        character_info['ability_list'] = {}
        character_info['ability_list']['ability_id'] = a.ability_id
        character_info['ability_list']['ability_value'] = a.ability_value
        character_info['ability_list']['ability_note'] = a.ability_note
        
    for w in character.weakness_list:
        character_info['weakness_list'] = {}
        character_info['weakness_list']['weakness_id'] = w.weakness_id #DA.getWeaknesses().get(w.weakness_id).name
        character_info['weakness_list']['weakness_value'] = w.weakness_value
        character_info['weakness_list']['weakness_note'] = w.weakness_note

    for a in character.attack_list:
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
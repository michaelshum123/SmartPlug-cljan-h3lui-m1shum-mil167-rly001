# lab/lab.py

import os
from flask import Flask, render_template, g, request, redirect, jsonify
from sqlite3 import dbapi2 as sqlite3
from datetime import date
from . import sensordb
import json
##### APP SETUP #####
app = Flask(__name__)

##### DB SETUP #####

# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'potatosalad'),
    DEBUG=True,
    SECRET_KEY=b'<SOME HEXADECIMAL SECRET KEY>', #wait what
    USERNAME='admin',
    PASSWORD='<SOME PASSWORD>' #works everytime!
))

# Connect to the DB
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def get_sdb():
    if not hasattr(g,'sdb'):
        g.sdb = sensordb.sensordb()
    return g.sdb
# Create the database (we do this via command line!!!)
def init_db():
    """Initializes the database."""
    #db = get_db()
    #with app.open_resource('schema.sql', mode='r') as f:
    #db.cursor().executescript(f.read())
    #db.commit()
    s = get_sdb()
    s.makeTables()

# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

##### ROUTES #####
@app.route('/')
def home():
    s = get_sdb()
    dht  = s.get_DHT22(1)
    temp = dht[0][1]
    water = False
    if dht[0][2] < 20:
        water = True
    light = 0.0
    photos = s.get_Photo(60*24) #assumes 1 reading every minute

    startdate = photos[-1][0][:10] #get most recent reading

    today = [d for d in photos if d[0][:10]==startdate and d[1] > 800]
    startTime = today[0][0].split()[1].split(":")[0]
    endTime   = today[-1][0].split()[1].split(":")[0]
    light =int( endTime) - int(startTime)

    datestr = date.today().strftime("%B %d, %Y")
    return render_template('home.html',doWater=water,light=light,date=datestr, temp=temp )
@app.route('/viewall')
def viewall():
    s = get_sdb()
    dht = s.get_DHT22(-1)
    photo = s.get_Photo(-1)
    return render_template('viewall.html',dht=dht,photo=photo)
'''
@app.route('/dht')
def show_dht():
    s = get_sdb()

    dht = s.get_DHT22(-1)
    sound = []
    photo = []

    return render_template('home.html',dht=dht, sound=sound, photo=photo)

@app.route('/photo')
def show_photo():
    s = get_sdb()

    dht = []
    sound = []
    photo = s.get_Photo(-1)

    return render_template('home.html',dht=dht, sound=sound, photo=photo)

@app.route('/sound')
def show_sound():
    s = get_sdb()

    dht = []
    sound = s.get_Sound(-1)
    photo = []

    return render_template('home.html',dht=dht, sound=sound, photo=photo)
'''
@app.route('/rest_dht', methods=['GET','POST'])
def rest_dht():
    s = get_sdb()
    if request.method == 'GET':
        count = request.args.get('count', default=5, type=int)
        output = []
        for r in s.get_DHT22(count):
            newRow = {'date':r[0], 'temp':r[1], 'hum':r[2]}
            output.append(newRow)
        return jsonify(output)
    elif request.method == 'POST':
        temp = request.form.get('temp')
        hum  = request.form.get('hum')
        print(temp)
        print(hum)
        s.set_DHT22(temp, hum)
        return jsonify({"success":True})

@app.route('/rest_sound',methods=['GET','POST'])
def rest_sound():
    s = get_sdb()
    if request.method == 'GET':
        count = request.args.get('count', default=5, type=int)
        output = []
        for r in s.get_Sound(count):
            newRow = [r[0], r[1], r[2], r[3]]
            output.append(newRow)
        return jsonify(output)
    elif request.method == 'POST':
        data = request.get_json()
        if not( 'audio' in data and 'env' in data and 'gate' in data):
            return jsonify({"success":False,"msg":"A value(s) could not be found"})
        s.set_Sound(data['audio'],data['env'],data['gate'])
        return jsonify({"success":True})

@app.route('/rest_photo',methods=['GET','POST'])
def rest_photo():
    if request.method == 'GET':
        count = request.args.get('count', default=5, type=int)
        output = []
        for r in s.get_Photo(count):
            newRow = [r[0], r[1]]
            output.append(newRow)

        return jsonify(output)
    elif request.method == 'POST':
        data = request.get_json()
        s.set_Photo(data['light'])
        return jsonify({"success":True})



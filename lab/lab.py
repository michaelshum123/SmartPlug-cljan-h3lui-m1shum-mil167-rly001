# lab/lab.py

import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3
from . import sensordb
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
        g.sdb = sensordb()
    return g.sdb()
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
    dht = s.get_DHT22(10)
    sound = s.get_Sound(10)
    photo = s.get_Photo(10)

    return render_template('home.html',dht=dht, sound=sound, photo=photo)

@app.route('/get_example')
def GET_Example() :
    db = get_db()
    cur = db.execute('SELECT first_name, last_name, age FROM users ORDER BY id DESC')
    the_users = cur.fetchall()
    return render_template('get_example.html', entries=the_users)

@app.route('/post_example', methods=['POST'])
def POST_Example():
    db = get_db()
    db.execute('INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)',
                 [request.form['first'], request.form['last'], request.form['age']])
    db.commit()
    return redirect('/get_example')

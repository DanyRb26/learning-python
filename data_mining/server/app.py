from flask import Flask, render_template
from database import Con, cur
import sqlite3
from flask import g 

app = Flask(__name__)

DATABASE = 'market.db'

def get_bd ():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        return db
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.route('/')
def index ():
    Con = get_db()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    return render_template('cliente/index.html', None)

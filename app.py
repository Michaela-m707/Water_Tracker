
from flask import Flask, request, render_template

app = Flask(__name__)

import sqlite3
import json

# http://10.80.23.119:41973/

db = sqlite3.connect("watertracker.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

@app.route('/')
def index():

    data = cursor.execute("SELECT * FROM water_intake").fetchall()
    
    # Temporary data processing
    output = []
    for row in data:
        output.append(list(row))
    return output

@app.route('/add')
def add():
    return render_template('add.html', title="Add Record")

if __name__ == '__main__':
    app.run(debug=True, port=41973, host='0.0.0.0')

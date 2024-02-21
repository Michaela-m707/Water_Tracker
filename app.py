
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

    data = request.form
    
    date = None

    if "date" in data:
        date = data["date"]

    if not "user_id" in data:
        return "User ID Missing"

    if not "intake_amount" in data:
        return "Intake Amount Missing"
    
    if date == None:

        cursor.execute("INSERT into water_intake (user_id, intake_amount) VALUES (?, ?)", (data["user_id"], data["intake_amount"]))
    else:

        cursor.execute("INSERT into water_intake (date, user_id, intake_amount) VALUES (?, ?, ?)", (data["date"], data["user_id"], data["intake_amount"]))

    db.commit()

    return "Record Added"

@app.route('/add-submit')
def add_submit():
    return "Record Added <h1><a href=\"/\">Home</a></h1>"

if __name__ == '__main__':
    app.run(debug=True, port=41973, host='0.0.0.0')

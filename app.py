
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
    
    # Date is optional
    date = None
    
    if "date" in data:
        date = data["date"]
    
    # Intake Amount must exist
    if not "intake_amount" in data:
        return "Intake Amount Missing"

    # Get Username

    if not "username" in data:
        return "Username Missing"

    user = cursor.execute("SELECT * from users WHERE username LIKE ?", (data["username"],)).fetchone()
    
    if user == None:
        return "Invalid User"

    user_id = user["id"]
     
    
    if date == None:
        cursor.execute("INSERT into water_intake (user_id, intake_amount) VALUES (?, ?)", (user_id, data["intake_amount"]))
    else:

        cursor.execute("INSERT into water_intake (date, user_id, intake_amount) VALUES (?, ?, ?)", (data["date"], user_id, data["intake_amount"]))

    db.commit()

    return "Record Added"

@app.route('/add-submit')
def add_submit():
    return "Record Added <h1><a href=\"/\">Home</a></h1>"

if __name__ == '__main__':
    app.run(debug=True, port=41973, host='0.0.0.0')

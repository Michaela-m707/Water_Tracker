
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', title="Water Tracker")

@app.route('/add')
def add():
    return render_template('add.html', tittle="Add Record")

if __name__ == '__main__':
    app.run(debug=True, port=41973, host='0.0.0.0')

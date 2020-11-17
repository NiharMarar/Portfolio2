#imports
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/navbar')
def navbar():
    return render_template("base.html")

@app.route('/Hello-Series')
def HelloSeries():
    return render_template("HelloSeries.html")

@app.route('/Flask-Series')
def FlaskSeries():
    return render_template("FlaskSeries.html")
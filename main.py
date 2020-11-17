#imports
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/navbar')
def navbar():
    return render_template("base.html")


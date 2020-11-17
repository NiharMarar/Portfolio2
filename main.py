#imports
from flask import Flask, redirect, url_for , render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/navbar')
def navbar():
    return render_template("base.html")

@app.route('/Hello-Series')
def HelloSeries():
    return render_template("HelloSeries.html")

@app.route('/Flask-Series')
def FlaskSeries():
    return render_template("FlaskSeries.html")

if __name__ == "__main__":
    app.run(debug=True,port='8080')
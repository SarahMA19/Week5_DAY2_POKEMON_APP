from app import app

from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/finder')
def pokemonfinderPage():
    return render_template('finder.html')
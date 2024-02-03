from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():

    #return to an html file - asking for user input 
    #return "Hello, World!"

    
    return render_template('first.html', title='Home')

@app.route('/output')
def output():
    return render_template('output.html', title='Home')

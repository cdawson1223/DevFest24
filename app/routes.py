from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():

    #return to an html file - asking for user input 
    #return "Hello, World!"
    print("in this route")

    '''if 'submitButton' and request.form['submitButton'] == 'clicked':
        print("in this if")
        size = request.form.get('dropdown1')
        weather = request.form.get('dropdown2')
        cost = request.form.get('dropdown3')
        demographic = request.form.get('dropdown4')
        walkability = request.form.get('dropdown5')
        safety = request.form.get('dropdown6')
        public_transportation = request.form.get('dropdown7')
        my_list [size,weather, cost, demographic, walkability, safety, public_transportation]
        return redirect(url_for('destination',parameters = my_list))'''

    return render_template('first.html', title='Home')

@app.route('/submit', methods=['POST'])
def submit():
    if request.form['submitButton'] == 'clicked':
        print("in this if")
        size = request.form.get('dropdown1')
        weather = request.form.get('dropdown2')
        cost = request.form.get('dropdown3')
        demographic = request.form.get('dropdown4')
        walkability = request.form.get('dropdown5')
        safety = request.form.get('dropdown6')
        public_transportation = request.form.get('dropdown7')
        my_list = [size,weather, cost, demographic, walkability, safety, public_transportation]
        #return redirect(url_for('destination',parameters = my_list))
        return render_template('output.html', title='Home', my_list=my_list)
    return render_template('first.html', title='Home')
    




'''@app.route('/destination/<parameters>',methods=['POST'])
def destination(parameters):
    #input types 
    #generate all 7 
    size = request.form.get('dropdown1')
    weather = request.form.get('dropdown2')
    cost = request.form.get('dropdown3')
    demographic = request.form.get('dropdown4')
    walkability = request.form.get('dropdown5')
    safety = request.form.get('dropdown6')
    public_transportation = request.form.get('dropdown7')
    #input the 7 into our decision making model 
    my_list [size,weather, cost, demographic, walkability, safety, public_transportation]
    #output 4 best cities 

    city = "New York City"
    return render_template('output.html', title='Home', my_list=parameters)'''

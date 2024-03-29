from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField('Generate Cty!')


    #junk 
    <!doctype html>
<html>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <head>
        <title>Where to live</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
        body {
            /* Set background image and properties */
            /*background-image: url('nycskyline.jpeg');*/ /* Replace 'path/to/your/image.jpg' with the actual path to your image */
            background-image: url("{{ url_for('static', filename='nycskyline.jpg') }}");
            background-size: cover; /* Adjust as needed: cover, contain, or a specific size */
            background-position: center center; /* Adjust as needed: center center, top left, etc. */
            background-repeat: no-repeat; /* Prevent image repetition */
            height: 100vh; /* Set the height to the full viewport height */
            margin: 0; /* Remove default margin */
            display: flex;
            align-items: center;
            justify-content: center;
            color: black; /* Set text color to contrast with the background */
        }
        label {
            color: white;
            font-weight: bold;
        }
        /* Add additional styling as needed */

    </style>
    </head>
    <div class="container mt-5" style="background-color: white;"></div>
    <body>
        <div class="container mt-5" style="background-color: white;color: black;">
        <h1>Hello, Welcome to pick a location to live!</h1>
        <h5>This platform allows for you to input what you want for where you live. Simply use the dropdowns for each category, and our algorithm will tell you the best place to live!</h2> 
        </div>
        <div class="container mt-5">
        <form method="post" action="/submit">
            
            <div class="mb-3">


                
            <label for="dropdown1">Size:</label>
            <select id="dropdown1" name="dropdown1">
                <option value="Small">Small</option>
                <option value="Medium">Medium</option>
                <option value="Large">Large</option>
            </select>
            <br>
        </div>
            
            <div class="mb-3">
            <label for="dropdown2" >Weather:</label>
            <select id="dropdown2" name="dropdown2">
                <option value="Cold">Cold</option>
                <option value="Hot">Hot</option>
                <option value="Don't Care">Don't Care</option>
            </select>
            <br>
        </div>
            

            <div class="mb-3">
            <label for="dropdown3" >Cost of Living:</label>
            <select id="dropdown3" name="dropdown3">
                <option value="Very Important">Very Important</option>
                <option value="Moderately Important">Moderately Important</option>
                <option value="Mildy Important">Mildy Important</option>
                <option value="Not Important">Not Important</option>
            </select>
            <br>
        </div>
    
            <div class="mb-3">
            <label for="dropdown4" style="color: blue">Demographics:</label>
            <select id="dropdown4" name="dropdown4">
                <option value="Predominatly White">Predominatly White</option>
                <option value="Predominatly Hispanic">Predominatly Hispanic</option>
                <option value="Predominatly Black">Predominatly Black</option>
                <option value="Predominatly Asian">Predominatly Asian</option>
                <option value="Mixed">Mixed</option>
            </select>
            <br>
        </div>
    
            <div class="mb-3">
            <label for="dropdown5" style="color: blue">Walkability:</label>
            <select id="dropdown5" name="dropdown5">
                <option value="Very Important">Very Important</option>
                <option value="Moderately Important">Moderately Important</option>
                <option value="Mildy Important">Mildy Important</option>
                <option value="Not Important">Not Important</option>
            </select>
            <br>
        </div>

            <div class="mb-3">
            <label for="dropdown6" style="color: blue">Safety:</label>
            <select id="dropdown6" name="dropdown6">
                <option value="Very Important">Very Important</option>
                <option value="Moderately Important">Moderately Important</option>
                <option value="Mildy Important">Mildy Important</option>
                <option value="Not Important">Not Important</option>
            </select>
            <br>
        </div>
            
            <div class="mb-3">
            <label for="dropdown7" >Public Transportation:</label>
            <select id="dropdown7" name="dropdown7">
                <option value="Very Important">Very Important</option>
                <option value="Moderately Important">Moderately Important</option>
                <option value="Mildy Important">Mildy Important</option>
                <option value="Not Important">Not Important</option>
            </select>
            <br>
        </div>
    
            <button type="submit" name="submitButton" value="clicked">Submit</button>
        </form>
        </div>
    </body>
    
</html>
import os
import os.path
from collections import defaultdict
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np 




"""
This will read all the csv files in the training directory and generate the hash map for thriving and missing directories

"""
def read_files(train_dir):

    # create the count for each city
    cities = dict()

    for f in os.listdir(train_dir):
        print(f)
        filename = train_dir + "/" + f
        print(filename)
        with open(filename, "r") as my_file:

            for line in my_file:

                stripped_line = line.split()

                # Take into account cases where the city is 2 words
                if len(stripped_line) == 12:
                    thriving_demo = stripped_line[4]
                    city = stripped_line[1] + " " + stripped_line[2]
                    city = city.strip(',')
                else:
                    thriving_demo = stripped_line[3]
                    city = stripped_line[1].strip(',')
                
                # remove the period at the end of the sentence
                fewer_demo = stripped_line[len(stripped_line) - 1].strip('.')

                # Add the thriving and missing demographic (if they exist) to the city data (if it exists)
                # Sets it to 1 if not
                if city in cities:
                    
                    if thriving_demo in cities[city]:
                        cities[city][thriving_demo] += 1
                    else:
                        cities[city][thriving_demo] = 1
                    
                    if fewer_demo in cities[city]:
                        cities[city][fewer_demo] -= 1
                    else:
                        cities[city][fewer_demo] = -1
                else:
                    cities[city] = dict()
                    cities[city][thriving_demo] = 1
                    cities[city][fewer_demo] = -1
    

    # Ensure all four groups are contained within each city
    groups = ("Asian", "Black", "White", "Hispanic")
    for city in cities:
        for group in groups:
            
            if not group in cities[city]:
                cities[city][group] = 0
    
    return cities


def regression(user_input):
    
    city_demo_data = read_files("demographic-data")
    
    city_value = 1
    
    df = pd.DataFrame()
    groups = ["Asian", "Black", "White", "Hispanic"]
    
    df["City"] = [i for i in range(1, 51)]
    
    np.random.seed(42)

# Create a DataFrame with random numbers
    data = {
        'Size': np.random.uniform(-0.5, 0.5, 50),
        'Weather': np.random.uniform(-0.5, 0.5, 50),
        'Cost of Living': np.random.uniform(-0.5, 0.5, 50),
        'Walkability': np.random.uniform(-0.5, 0.5, 50),
        'Safety': np.random.uniform(-0.5, 0.5, 50),
        'Public Transportation': np.random.uniform(-0.5, 0.5, 50)
    }

    df2 = pd.DataFrame(data)

    # add the data
    for group in groups:
        df[group] = [city_demo_data[city][group] for city in city_demo_data]
    
    df = pd.merge(df, df2)
    df.style
    
    # Split the data into training and testing sets
    X = df[['Asian', 'Black', 'White', "Hispanic", "Size", "Weather", "Cost of Living", "Walkability", "Safety", "Public Transportation"]]  # Include all the predictor variables you have
    y = df['City']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # # Print the coefficients
    # print("Coefficients:", model.coef_)
    # print("Intercept:", model.intercept_)

    # # Make predictions on the test data
    prediction = model.predict(user_input)

    # # Evaluate the performance
    #mse = mean_squared_error(y_test, predictions)
    # print("Mean Squared Error:", mse)
    return prediction

if __name__ == "__main__":
    regression()
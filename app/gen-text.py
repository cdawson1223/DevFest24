import random

def generate_sentence(city, states):
    demographics = ["White", "Black", "Hispanic", "Asian"]
    thriving_demographic = random.randint(0, 3)
    missing_demographic = random.randint(0, 3)
    sentence = f"In {city}, the {demographics[thriving_demographic]} is thriving, while there are few {demographics[missing_demographic]}."
    return sentence

def generate_file(file_name, cities, states):
    with open(file_name, 'w') as file:
        for city in cities:
            sentence = generate_sentence(city, states)
            file.write(sentence + '\n')

def main():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Detroit",
              "Jacksonville", "Indianapolis", "Columbus", "Austin", "Charlotte", "Memphis", "Baltimore", "Boston", "Seattle", "Denver",
              "Nashville", "Milwaukee", "Portland", "Oklahoma City", "Las Vegas", "Louisville", "Birmingham", "Raleigh", "Richmond", "Hartford",
              "New Orleans", "Buffalo", "Rochester", "Salt Lake City", "Grand Rapids", "Tucson", "Tulsa", "Fresno", "Wichita", "Albuquerque",
              "Omaha", "Bakersfield", "Knoxville", "Tampa", "Aurora", "Santa Ana", "Pittsburgh", "Cincinnati", "Anchorage", "Toledo"]

    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
              "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
              "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
              "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

    for i in range(1, 201):
        file_name = f"demographic-data/Demographics_{i}.txt"
        generate_file(file_name, cities, states)

if __name__ == "__main__":
    main()
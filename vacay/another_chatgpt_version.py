"""
Almost correct except the ratings should have some non-uniform distribution

The game revolves around the player trying to guess if he's pulled a near maximum from an unknown distribution
after seeing a few samples.

It is the classic optimal-stopping problem
"""
import random

cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
hotels = {"New York City": ["The Plaza", "The Ritz-Carlton", "The Waldorf Astoria"],
          "Los Angeles": ["The Beverly Hills Hotel", "The Four Seasons", "The Ritz-Carlton"],
          "Chicago": ["The Ritz-Carlton", "The Four Seasons", "The Peninsula"],
          "Houston": ["The Ritz-Carlton", "The Four Seasons", "The St. Regis"],
          "Phoenix": ["The Ritz-Carlton", "The Four Seasons", "The Canyon Suites"],
          "Philadelphia": ["The Ritz-Carlton", "The Four Seasons", "The Logan"],
          "San Antonio": ["The Ritz-Carlton", "The Four Seasons", "The St. Anthony"],
          "San Diego": ["The Ritz-Carlton", "The Four Seasons", "The Hotel Del Coronado"],
          "Dallas": ["The Ritz-Carlton", "The Four Seasons", "The Mansion on Turtle Creek"],
          "San Jose": ["The Ritz-Carlton", "The Four Seasons", "The Fairmont"]}
restaurants = {"New York City": ["Per Se", "Eleven Madison Park", "Le Bernardin"],
               "Los Angeles": ["Providence", "Osteria Mozza", "Spago"],
               "Chicago": ["Alinea", "Grace", "Topolobampo"],
               "Houston": ["Underbelly", "Uchi", "Killen's"],
               "Phoenix": ["Barrio Cafe Gran Reserva", "Pizzeria Bianco", "Kai"],
               "Philadelphia": ["Fork", "Oloroso", "Vetri"],
               "San Antonio": ["Cured", "La Panaderia", "Grayze"],
               "San Diego": ["Addison", "The Grill", "Eddie V's"],
               "Dallas": ["FT33", "The French Room", "Knife"],
               "San Jose": ["Manresa", "SingleThread", "Sons & Daughters"]}

def generate_vacation():
    city = random.choice(cities)
    hotel = random.choice(hotels[city])
    restaurant = random.choice(restaurants[city])
    return (city, hotel, restaurant)

def score_vacation(vacation):
    city, hotel, restaurant = vacation
    city_score = cities.index(city) + 1
    hotel_score = hotels[city].index(hotel) + 1
    restaurant_score = restaurants[city].index(restaurant) + 1
    return city_score * hotel_score * restaurant_score

def play_game():
    vacation = generate_vacation()
    max_score = len(cities) * 3 * 3
    score = score_vacation(vacation)
    print("You're going on vacation to:")
    print(f"City: {vacation[0]}")
    print(f"Hotel: {vacation[1]}")
    print(f"Restaurant: {vacation[2]}")
    print(f"Score: {score}/{max_score}")
    choice = input("Would you like to keep this vacation? (y/n) ")
    if choice.lower() == "y":
        print(f"You chose to keep your vacation! Your score is {score/max_score*100:.2f}% of the maximum score.")
    else:
        play_game()


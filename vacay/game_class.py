"""
Main game look and basic persistence
"""
import random
from vacay.worlds import cities

class Player(object):
    def __init__(self):
        # money to spend on travel
        self.money = 1000

        # no one gets out alive
        self.alive = True

        # Per month
        self.disposable_income = 500

        self.leave_days = 15


class Game(object):
    def __init__(self):
        self.player = Player()
        self.world = cities

    def go(self):
        print("You are going to ")
        city = random.choice(cities)
        print(city["name"])

        print()
        print("Sleeping at {0}")

        hotel = random.choice(city["hotels"])
        print(hotel["name"])
        print("Lunch at")
        lunch = random.choice(city["restaurants"])
        print(lunch["name"])
        print("Dinner at")
        dinner = random.choice(city["restaurants"])
        print(dinner["name"])
        print()

        spent = self.status(hotel, [lunch, dinner])
        print("You spent $" + str(spent))

        print("Next time, go to ")
        city = random.choice(cities)
        print(city["name"])

    def status(self, hotel, restaurants):
        spent = hotel["price"]
        for restaurant in restaurants:
            if restaurant:
                spent += restaurant["price"]
        return spent

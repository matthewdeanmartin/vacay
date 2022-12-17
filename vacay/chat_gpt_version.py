import random

hotels = [("Hilton", 5), ("Marriott", 4), ("Hyatt", 3), ("Holiday Inn", 2), ("Motel 6", 1)]
restaurants = [("Olive Garden", 5), ("Applebee's", 4), ("Chili's", 3), ("TGI Friday's", 2), ("McDonald's", 1)]
events = [("Amusement Park", 5), ("Zoo", 4), ("Museum", 3), ("Beach", 2), ("Park", 1)]

def generate_vacation():
  possible_combinations = [(hotel[0], restaurant[0], event[0]) for hotel in hotels for restaurant in restaurants for event in events]
  vacation = random.choice(possible_combinations)
  possible_combinations.remove(vacation)
  score = sum(hotel[1] for hotel in hotels if hotel[0] == vacation[0]) + \
          sum(restaurant[1] for restaurant in restaurants if restaurant[0] == vacation[1]) + \
          sum(event[1] for event in events if event[0] == vacation[2])
  return (vacation[0], vacation[1], vacation[2], score)

max_score = sum(hotel[1] for hotel in hotels) + sum(restaurant[1] for restaurant in restaurants) + sum(event[1] for event in events)
vacation = generate_vacation()
print(f"Your vacation includes a stay at the {vacation[0]}, a meal at {vacation[1]}, and a visit to {vacation[2]} for a total score of {vacation[3]}.")

rejections = 0
while True:
  answer = input("Would you like to keep this vacation or try again? (keep/try again)")
  if answer.lower() == "keep":
    print(f"Great, have a fantastic vacation! Your maximum possible score was {max_score}, and your actual score was {vacation[3]}.")
    print(f"You rejected {rejections} vacations out of {len(hotels) * len(restaurants) * len(events) - rejections} possible combinations.")
    break
  elif answer.lower() == "try again":
    rejections += 1
    if len(possible_combinations) == 0:
      print(f"There are no more possible vacations left. Your maximum possible score was {max_score}, and your actual score was {vacation[3]}.")
      print(f"You rejected {rejections} vacations out of {len(hotels) * len(restaurants) * len(events)} possible combinations.")
      break
    else:
      vacation = generate_vacation()
      print(f"Your new vacation includes a stay at the {vacation[0]}, a meal at {vacation[1]}, and a visit to {vacation[2]} for a total score of {vacation[3]}.")
  else:
    print("Invalid input. Please enter 'keep' or 'try again'.")

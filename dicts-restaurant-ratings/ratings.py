"""Restaurant rating lister."""
import random

# put your code here
def display_rating1(filename):
    restaurant_rating = {}
    data = open(filename)
    for line in data:
        restaurants = line.rstrip().split(":")[0]
        ratings = line.rstrip().split(":")[1]
        restaurant_rating[restaurants] = int(ratings)
    for resataurant, rating in sorted(restaurant_rating.items()):
            print(f"{resataurant} is rated at {rating}")
    return sorted(restaurant_rating)

def display_rating2(filename):
    restaurant_rating = {}
    data = open(filename)
    for line in data:
        restaurants = line.rstrip().split(":")[0]
        ratings = line.rstrip().split(":")[1]
        restaurant_rating[restaurants] = int(ratings)
    return restaurant_rating

def add_restaurant_score(restaurant_rating):
    user_restaurant = input("Please enter restaurant name: ").title()
    while True:
        user_score = int(input("Please enter restaurant rating: "))
        if user_score not in range(1,6):
            print("Please enten rating between 1 to 5!")
            continue
        restaurant_rating[user_restaurant] = user_score
        for resataurant, rating in sorted(restaurant_rating.items()):
            print(f"{resataurant} is rated at {rating}")
        break

def update_rating(restaurant_rating):
    while True:
        restaurant, rating = random.choice(list(restaurant_rating.items()))
        print(f"The current rating of {restaurant} is {rating}")
        update = int(input("Please update the rating: "))
        if update not in range(1, 6):
            print("Please enten rating between 1 to 5!")
            continue
        else:
            restaurant_rating[restaurant] = update
            print(f"Now {restaurant} is rated at {update}")
        break

def user_update(restaurant_rating):
    print(restaurant_rating)
    while True:
        user_choose = input("Please choose which restaurant you want to update rating: ").title()
        update = int(input("Please enter new rating: "))
        if update not in range(1, 6):
            print("Please enten rating between 1 to 5!")
            continue
        else:
            for restaurant, _ in restaurant_rating.items():
                if user_choose == restaurant:
                    restaurant_rating[restaurant] = update
                    print(f"Now {restaurant} is rated at {update}")
        break
    
        
            
    
    
#restaurant_rating = display_rating2("scores.txt")
#update_rating(restaurant_rating)

def user_choice():
    while True:
        choice = int(input("What do you want to choose 1- see all ratings, 2- add a new restaurant, 3- update random rating,4- choose and update, 5- quit?  "))
        if choice == 1:
            display_rating1("scores.txt")
        elif choice == 2:
            restaurant_rating = display_rating2("scores.txt")
            add_restaurant_score(restaurant_rating)
        elif choice == 3:
            restaurant_rating = display_rating2("scores.txt")
            update_rating(restaurant_rating)
        elif choice == 4:
            restaurant_rating = display_rating2("scores.txt")
            user_update(restaurant_rating)
        elif choice == 5:
            break
        
user_choice()        


# restaurant_rating = display_rating("scores.txt")     
# add_restaurant_score(restaurant_rating)
            

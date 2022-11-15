"""Restaurant rating lister."""


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
    return

def user_choice():
    choice = int(input("What do you want to choose 1- see all ratings, 2- add a new restaurant, 3- quit? "))
    if choice == 1:
        return display_rating1("scores.txt")
    elif choice == 2:
        restaurant_rating = display_rating2("scores.txt")
        add_restaurant_score(restaurant_rating)
    elif choice == 3:
        exit
        
user_choice()        


# restaurant_rating = display_rating("scores.txt")     
# add_restaurant_score(restaurant_rating)
            

#Ibai
#madlibs
#Create a story using user inputs

#Init
import random
#Functions

def madlibs():


    adjectives = [ "big", "small", "large", "tiny", "old", "new", "young", "ancient", "good"
, "bad", "happy", "sad", "easy", "hard", "hot", "cold", "clean", "dirty", "funny", "fast", "slow", "loud", "quiet", "strong", "weak", "bright", "dark"]
    places = ["Chicago", "McDonalds", "Jones", "Home", "Costco"]
    foods = ["pasta", "burgers", "steak", "ice cream", "salad", "ribs"]
    names = ["IBK", "Nathan", "Evan", "Aedric", "Valerie", "Veronika", "Sophia", "Maya", "Nikolas", "Diego"]


    adjective1 = input("Adjective: ").upper()
    if adjective1 == "RANDOM":
        adjective1 = random.choice(adjectives).upper()

    name1 = input("Name: ").upper()
    if name1 == "RANDOM":
        name1 = random.choice(names).upper()

    adjective2 = input("Adjective: ").upper()
    if adjective2 == "RANDOM":
        adjective2 = random.choice(adjectives).upper()

    place1 = input("Place: ").upper()
    if place1 == "RANDOM":
        place1 = random.choice(places).upper()

    food1 = input("Food: ").upper()
    if food1 == "RANDOM":
        food1 = random.choice(foods).upper()

    place2 = input("Place: ").upper()
    if place2 == "RANDOM":
        place2 = random.choice(places).upper()

    adjective3 = input("Adjective: ").upper()
    if adjective3 == "RANDOM":
        adjective3 = random.choice(adjectives).upper()



    print(f"""Me and my \033[1m{adjective1}\033[0m friend \033[1m{name1}\033[0m had a \033[1m{adjective2}\033[0m adventure to \033[1m{place1}\033[0m.
We ate \033[1m{food1}\033[0m then went to \033[1m{place2}\033[0m.
Overall it was a \033[1m{adjective3}\033[0m day.""")





#Main
madlibs()

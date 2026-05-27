#Ibai
#search.py
#Init
import random
low = 1
high = 100
secret_number = random.randint(low,high)
#Functions

def linear_search():
    attempts = 1
    for guess in range(1, 100):
        if secret_number != guess:
            attempts = attempts + 1
        else:
            print(f"The secret number is {guess}")
            print(f"It took {attempts} attempts to find it")

def binary_search():
    global high
    global low
    attempts = 1
    found = False
    while found == False:
        mid = (high + low) // 2
        if mid == secret_number:
            print(f"The secret number is {mid}")
            print(f"It took {attempts} attempts to find it")
            found = True
        elif mid < secret_number:
            low = mid + 1
            attempts = attempts + 1
        elif mid > secret_number:
            high = mid -1
            attempts = attempts + 1


#Main
linear_search()
binary_search()



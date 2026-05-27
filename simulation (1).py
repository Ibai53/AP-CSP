#Ibai
#race.py

#Initialize

import random
finish_line = 50
tortoise_pos = 0
hare_pos = 0
is_hare_asleep = False
hare_wins = 0
snail_wins = 0
tortoise_wins = 0
hare_sleep = 57
snail_pos = 0
snail_ride = 50

#Functions
def race():
    global finish_line
    global tortoise_pos
    global hare_pos
    global is_hare_asleep
    global hare_wins
    global tortoise_wins
    global snail_pos
    global snail_ride
    global snail_wins
    while tortoise_pos < finish_line and hare_pos < finish_line:
        tortoise_pos = tortoise_pos + random.randint(1,3)
        sleep = random.randint(1,100)
        if sleep <= hare_sleep:
            is_hare_asleep = True
        else:
            is_hare_asleep = False
        if is_hare_asleep == False:
            hare_pos = hare_pos + random.randint(1,10)
        ride = random.randint(1,100)
        if ride <= snail_ride:
            snail_pos = hare_pos
    if tortoise_pos >= finish_line:
        #print("Tortoise Wins!")
        tortoise_wins = tortoise_wins + 1
    elif snail_pos >= finish_line:
        snail_wins = snail_wins + 1
    else:
        #print("Hare Wins!")
        hare_wins = hare_wins + 1

def simulate(number):
    global hare_wins
    global tortoise_wins
    global tortoise_pos
    global hare_pos
    global is_hare_asleep
    global snail_pos
    for i in range(number):
        tortoise_pos = 0
        hare_pos = 0
        snail_pos = 0
        is_hare_asleep = False
        race()
    print(f"Hare wins: {hare_wins}")
    print(f"Tortoise wins: {tortoise_wins}")
    print(f"Snail wins: {snail_wins}")
    print(f"Tortoise win percentage: {tortoise_wins/number*100}")
    print(f"Hare win percentage: {hare_wins/number*100}")
    print(f"Snail win percentage: {snail_wins/number*100}")

#Main
simulate(100000)

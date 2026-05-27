#Ibai and IBK
#Slot.py
#Create a slot machine

#Init
symbols = ["7", "🂡", "🂡", "💕", "💕", "💕", "🌙", "🌙", "🌙", "🌙", "🌙", "🌙", "🌙", "⚡", "⚡", "⚡", "⚡", "⚡", "⚡", "⚡", "⚡", "⚡"]
import random
money = 0
players = [""]
balances = [""]

#Functions
def menu():
    print("\nSpin")
    print("Balance")
    print("Deposit")
    print("Cashout")
    print("Simulate\n")

def simulate():
    global money
    winnings = 0
    wins = 0
    jackpots = 0
    simulations = int(input("How many simulations do you want to run?: "))
    for i in range(simulations):
        slot1 = random.choice(symbols)
        slot2 = random.choice(symbols)
        slot3 = random.choice(symbols)
        if slot1 == slot2 == slot3 == "7":
            winnings = winnings +300
            jackpots = jackpots + 1
        elif slot1 == slot2 == slot3:
            winnings = winnings + 50
            wins = wins + 1
    print(f"\nThe Player Spent {simulations*10}")
    print(f"\nThe Player Had {wins} Wins")
    print(f"\nThe Player Had {jackpots} Jackpots")
    print(f"The Player Won {winnings}")
    print(f"The Casino Has Made {simulations*10-winnings}")
    input("\nPress enter to continue")

def balance():
    global money
    print(f"\nYou have {money} credits in your account!\n")
    input("Press enter to continue")

def deposit():
    global money
    deposit = input("\nHow much would you like to deposit?(50, 100, 500): ")
    if deposit == "50":
        money = money + 50
        print("\n50 Credits have been added!")
    elif deposit == "100":
        money = money + 100
        print("\n100 Credits have been added!")
    elif deposit == "500":
        money = money + 500
        print("\n500 Credits have been added!")
    else:
        print("Invalid Input")
    input("\nPress enter to continue")




def spin():
    global money
    global slot1
    global slot2
    global slot3
    if money > 10:
        while True:
            spin = input("Press enter to spin!")
            if money < 10:
                break
            elif spin == "":
                money = money - 10
                slot1 = random.choice(symbols)
                print(slot1)
                slot2 = random.choice(symbols)
                print(slot2)
                slot3 = random.choice(symbols)
                print(slot3)
                if slot1 == "🂡" or slot2 == "🂡" or slot3 == "🂡":
                    wildcard()
                elif slot1 == slot2 == slot3 == "7":
                    print("JACKPOT!")
                    print("YOUT WON 300 CREDITS!")
                    money = money +300
                elif slot1 == slot2 == slot3:
                    print("YOU WIN!")
                    print("YOU WON 50 CREDITS")
                    money = money + 50
                else:
                    print("You Lose")
            else:
                print("Insufficient Funds")
                break
    else:
        print("Insufficient Funds")

def main():
    global slot1
    global slot2
    global slot3
    global money
    print("\nWelcome to the Casino!")
    name = input("What is your name: ")
    with open('casinoplayers.txt', 'r') as f:
        players = f.read().splitlines()


    with open('casinobalance.txt', 'r')  as f:
        balances = f.read().splitlines()
    try:
        index = players.index(name)
        print(index)
        money = int(balances[index])
        print(money)

    except:
        players.append(name)
        index = players.index(name)
        balances.append(money)
        print(index)
    while True:
        menu()
        action = input("What would you like to do?: ").upper()
        if action == "SPIN":
            spin()
        elif action == "BALANCE":
            balance()
        elif action == "DEPOSIT":
            deposit()
        elif action == "CASHOUT":
            balances[index] = str(money)
            with open('casinoplayers.txt', 'w') as txt_file:
                for i in range (len(players)):
                    txt_file.write(players[i] + "\n")

            with open('casinobalance.txt', 'w') as txt_file:
                for i in range (len(balances)):
                    txt_file.write(balances[i])
                    txt_file.write("\n")
            break
        elif action == "SIMULATE":
            simulate()
        else:
            print("Invalid Input")

def wildcard():
    global slot1
    global slot2
    global slot3
    global money
    if slot1 == "🂡":
        if slot2 == "7" and slot3 == "7":
            print("JACKPOT!")
            print("YOUT WON 300 CREDITS!")
            money = money +300
        elif slot2 == slot3:
            print("YOU WIN!")
            print("YOU WON 50 CREDITS")
            money = money + 50
        else:
            print("Wildcard extra spin!")
            input("Press enter to continue")
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            print(slot1)
            print(slot2)
            print(slot3)
            if slot2 == "7" and slot3 == "7":
                print("JACKPOT!")
                print("YOUT WON 300 CREDITS!")
                money = money +300
            elif slot2 == slot3:
                print("YOU WIN!")
                print("YOU WON 50 CREDITS")
                money = money + 50
            else:
                print("You Lose!")


    elif slot2 == "🂡":
        if slot1 == "7" and slot3 == "7":
            print("JACKPOT!")
            print("YOUT WON 300 CREDITS!")
            money = money +300
        elif slot1 == slot3:
            print("YOU WIN!")
            print("YOU WON 50 CREDITS")
            money = money + 50
        else:
            print("Wildcard extra spin!")
            input("Press enter to continue")
            slot1 = random.choice(symbols)
            slot3 = random.choice(symbols)
            print(slot1)
            print(slot2)
            print(slot3)
            if slot1 == "7" and slot3 == "7":
                print("JACKPOT!")
                print("YOUT WON 300 CREDITS!")
                money = money +300
            elif slot1 == slot3:
                print("YOU WIN!")
                print("YOU WON 50 CREDITS")
                money = money + 50
            else:
                print("You Lose!")

    elif slot3 == "🂡":
        if slot1 == "7" and slot2 == "7":
            print("JACKPOT!")
            print("YOUT WON 300 CREDITS!")
            money = money +300
        elif slot1 == slot2:
            print("YOU WIN!")
            print("YOU WON 50 CREDITS")
            money = money + 50
        else:
            print("Wildcard extra spin!")
            input("Press enter to continue")
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            print(slot1)
            print(slot2)
            print(slot3)
            if slot1 == "7" and slot2 == "7":
                print("JACKPOT!")
                print("YOUT WON 300 CREDITS!")
                money = money +300
            elif slot1 == slot2:
                print("YOU WIN!")
                print("YOU WON 50 CREDITS")
                money = money + 50
            else:
                print("You Lose!")




main()

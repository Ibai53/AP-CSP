#Ibai and IBK
#pokemon.py
#Pokemon game

#Initialize
day = 1
pokemon = "charmander"
level = 5
mood = 3
wins = 0
losses = 0
save = "pokemongamesave"
import random


#Functions

def main():
    while True:
        if (level >= 10 and pokemon == "charmander") or (level >= 20 and pokemon == "charmeleon"):
            evolve()
        action = 0
        menu()
        action = input("What would you like to do: ")
        if action == "train":
            train()
        elif action == "info":
            info()
        elif action == "end":
            break
        elif action == "gym":
            gym()
        elif action == "save":
            save_game()
        elif action == "load":
            load_game()
        elif action == "final":
            final()
            print("Thank you for playing!")
            break

def save_game():
    global pokemon
    global level
    global day
    global wins
    global losses
    global save
    global mood
    with open(save, "w") as file:  # Open the save file in write mode
        file.write(pokemon + "\n")  # Write the Pokémon's name
        file.write("Level:" + str(level) + "\n")  # Write the Pokémon's level
        file.write(str(day) + "\n")
        file.write(str(wins) + "\n")
        file.write(str(losses) + "\n")
        file.write(str(mood) + "\n")
    print("Game saved!")
    input("Press enter to continue")

def load_game():
      global pokemon
      global level
      global day
      global wins
      global losses
      global mood
      with open(save, "r") as file:  # Open the save file in read mode
            pokemon = file.readline().strip()  # Read the Pokémon's name
            level = int(file.readline().strip())
            day = int(file.readline().strip())
            wins = int(file.readline().strip())
            losses = int(file.readline().strip())
            mood = int(file.readline().strip())
      print("\n \n \n \n Game Loaded!")
      input("Press enter to continue")

def train():
    global level
    global pokemon
    global day
    level = level + 1
    print("\n \n \n")
    print(f"{pokemon} leveled up to level {level}")
    day = day + 1
    input("Press enter to continue")

def gym():
    global level
    global pokemon
    global day
    global mood
    global wins
    global losses
    print("\n \n \n \n")
    print("Bulbasaur wants to fight you")
    print(f"{pokemon} attacks with flamethrower")
    win = random.randint(1,14-mood)
    if win >= 5:
        wins = wins + 1
        print("Bulbasaur is defeated!")
        level = level + 2
        print(f"{pokemon} leveled up to level {level}!")
        mood = mood - 1
    else:
        print(f"{pokemon} is defeated! You lose!")
        losses = losses + 1
        mood = mood + 1
    day = day +1
    input("press enter to continue")

def final():
    global level
    global pokemon
    global wins
    global losses
    print("\n \n \n \n")
    print("You challenge Kyogre to a fight!")
    print(f"{pokemon} attacks Kyogre using dragon breath")
    win = random.randint(level-mood,35)
    if win >= 30:
        print("Kyogre is defeated!")
        print("Victory!")
        input("press enter to continue")
    else:
        print("Kyogre dodges it")
        print("Kyogre attacks with hyperbeam")
        print(f"{pokemon} is defeated!")
        print("Game Over")
        input("Press enter to continue")

def menu():
    global day
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    print(f"Day {day}")
    print("")
    print("Train")
    print("Gym Battle")
    print("Final Battle")
    print("Info")
    print("Load")
    print("Save")
    print("End")
    print(" ")

def evolve():
    global level
    global pokemon
    if (level >= 10 and pokemon == "charmander"):
        pokemon = "charmeleon"
        print("Charmander has evolved into charmeleon!")
        art(pokemon)
        input("press enter to continue")
    if (level >= 20 and pokemon == "charmeleon"):
        pokemon = "charzard"
        print("Charmeleon has evolved into charzard!")
        art(pokemon)
        input("press enter to continue")

def info():
    global pokemon
    global level
    global mood
    global day
    global wins
    global losses
    print("\n \n \n \n")
    print(f"{pokemon}")
    print(f"Level: {level}")
    if mood <= 4:
        print(f"{pokemon} is happy!")
    elif mood <= 8:
        print(f"{pokemon} is sad!")
    else:
        print(f"{pokemon} is furious!")
    print(f"{pokemon} has won {wins} battles")
    print(f"{pokemon} has lost {losses} battles")
    art(pokemon)
    day = day + 1
    input("Press enter to continue")

def art(stage):
    if stage == "charmander":
        print((r"             _.--\"\"`-..\n"))
        print((r"           ,'          `.\n"))
        print((r"         ,'          __  `.\n"))
        print((r"        /|          \" __   \\\n"))
        print((r"       , |           / |.   .\n"))
        print((r"       |,'          !_.'|   |\n"))
        print((r"     ,'             '   |   |\n"))
        print((r"    /              |`--'|   |\n"))
        print((r"   |                `---'   |\n"))
        print((r"    .   ,                   |                       ,\".\n"))
        print((r"     ._     '           _'  |                    , ' \\ `\n"))
        print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n"))
        print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n"))
        print(("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n"))
        print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,\n"))
        print((r"   `.      '            '            /          '    |'. |/\n"))
        print((r"     `.   |              \\       _,-'           |       ''\n"))
        print((r"       `._'               \\   '\"\\                .      |\n"))
        print((r"          |                '     \\                `._  ,'\n"))
        print((r"          |                 '     \\                 .'|\n"))
        print((r"          |                 .      \\                | |\n"))
        print((r"          |                 |       L              ,' |\n"))
        print((r"          `                 |       |             /   '\n"))
        print((r"           \\                |       |           ,'   /\n"))
        print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'\n"))
        print((r"        /     .             .      `!             ,j'\n"))
        print((r"       /       `.          /        .           .'/\n"))
        print((r"      .          `.       /         |        _.'.'\n"))
        print((r"       `.          7`'---'          |------\"'_.'\n"))
        print((r"      _,.`,_     _'                ,''-----\"'\n"))
        print((r"  _,-_    '       `.     .'      ,\\\n"))
        print((r"  -\" /`.         _,'     | _  _  _.|\n"))
        print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /\n"))
        print((r"                           `\" \" -' mh\n"))
        print(("\n"))
        print(("\n"))

    elif stage == "charmeleon":
        print((r"                     ,-'`\\\n"))
        print((r"                 _,\"'    j\n"))
        print((r"          __....+       /               .\n"))
        print((r"      ,-'\"             /               ; `-._.'.\n"))
        print((r"     /                (              ,'       .'\n"))
        print((r"    |            _.    \\             \\   ---._ `-.\n"))
        print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n"))
        print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l\n"))
        print((r" .,-        `._  |  |    |              \\       _   l .\n"))
        print((r"/              `\"--'    /              .'       ``. |  )\n"))
        print((".\\    ,                 |                .        \\ `. '\n"))
        print(("`.                .     |                '._  __   ;. \\'\n"))
        print((r" `-..--------...'       \\                  `'  `-\"'.  \\\n"))
        print((r"     `......___          `._                        |  \\\n"))
        print((r"              /`            `..                     |   .\n"))
        print((r"             /|                `-.                  |    L\n"))
        print((r"            / |               \\   `._               .    |\n"))
        print((r"          ,'  |,-\"-.   .       .     `.            /     |\n"))
        print((r"        ,'    |     '   \\      |       `.         /      |\n"))
        print((r"      ,'     /|       \\  .     |         .       /       |\n"))
        print((r"    ,'      / |        \\  .    +          \\    ,'       .'\n"))
        print((r"   .       .  |         \\ |     \\          \\_,'        / j\n"))
        print((r"   |       |  L          `|      .          `        ,' '\n"))
        print((r"   |    _. |   \\          /      |           .     .' ,'\n"))
        print((r"   |   /  `|    \\        .       |  /        |   ,' .'\n"))
        print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'\n"))
        print((r"   `. |___,`    /  `.   /`.       '          |  .'\n"))
        print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'\n"))
        print((r"               |        .'  / _/_|          .\n"))
        print((r"               `,       `\"'/\"'    \\          `.\n"))
        print((r"                 `,       '.       `.         |\n"))
        print((r"            __,.-'         `.        \\'       |\n"))
        print((r"           /_,-'\\          ,'        |        _.\n"))
        print((r"            |___.---.   ,-'        .-':,-\"`\\,' .\n"))
        print((r"                 L,.--\"'           '-' |  ,' `-.\\\n"))
        print((r"                                       `.' mh\n"))

    else:
        print((r"                .\"-,.__\n"))
        print((r"                `.     `.  ,\n"))
        print((r"             .--'  .._,'\"-' `.\n"))
        print((r"            .    .'         `'\n"))
        print((r"            `.   /          ,'\n"))
        print((r"              `  '--.   ,-\"'\n"))
        print((r"               `\"`   |  \\\n"))
        print((r"                  -. \\, |\n"))
        print((r"                   `--Y.'      ___.\n"))
        print((r"                        \\     L._, \\\n"))
        print((r"              _.,        `.   <  <\\                _\n"))
        print((r"            ,' '           `, `.   | \\            ( `\n"))
        print((r"         ../, `.            `  |    .\\`.           \\ \\_\n"))
        print((r"        ,' ,..  .           _.,'    ||\\l            )  '\".\n"))
        print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n"))
        print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n"))
        print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n"))
        print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `.\n"))
        print((r"   | /           |L__           |    |          / /          `. `.\n"))
        print((r"  , /            .   .          |    |         / /             ` `\n"))
        print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n"))
        print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n"))
        print((".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n"))
        print(("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n"))
        print(("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n"))
        print(("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n"))
        print(("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n"))
        print(("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n"))
        print(("||/            _,-------7 '              . |  `-'    l         /    `||\n"))
        print((". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n"))
        print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'\n"))
        print((r"         /      ,'      |               |,'    \\-.._,.'/'\n"))
        print((r"         .     /        .               .       \\    .''\n"))
        print((r"       .`.    |         `.             /         :_,'.'\n"))
        print((r"         \\ `...\\   _     ,'-.        .'         /_.-'\n"))
        print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /\n"))
        print((r"               .'        /\"'          |  \"'   '_\n"))
        print((r"              /_|.-'\\ ,\".             '.'`__'-( \\\n"))
        print((r"                / ,\"'\"\\,'               `/  `-.|\" mh\n"))


#Main
main()

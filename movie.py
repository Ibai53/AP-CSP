#movie.py
#Allow the user learn about a movie based on filters that they choose

#Initialize
import pandas as pd

#Import Data
data = pd.read_csv('IMDB.csv') #Import data
titleData = data['Series_Title'].tolist()
yearData = data['Released_Year'].tolist()
timeData = data['Runtime'].tolist()
genreData = data['Genre'].tolist()
ratingData = data['IMDB_Rating'].tolist()
overviewData = data['Overview'].tolist()
directorData = data['Director'].tolist()

#Put the actors into arrays
star1Data = data['Star1'].tolist()
star2Data = data['Star2'].tolist()
star3Data = data['Star3'].tolist()
star4Data = data['Star4'].tolist()

filter = [] #Set up filter array

#Set Placeholder Filters
ageFilter = 1000
minlengthFilter = 0
maxlengthFilter = 1000
genreFilter = ""
movieratingFilter = -1
directorFilter = ""
action = ""
repeat = True


#Runs the program
def main():
    global repeat

    #Introduce Program
    print("\nWelcome to Movie Picker!")
    print("Navigate the menus using numbers")
    input("\nPress Enter to Continue")

    #Loop the program
    while repeat == True:

        #Filter the Data
        filters()

        #Check if the user wants to end the program
        if repeat == False:
            print("\nThank you for using Movie Picker!\n")
            break

        #Continue the program
        else:
            #Check if anything was filtered
            if len(filter) == 0:
                print("\nNo Results Found. Try Using Different Filters.\n")
                input("Press Enter to Continue")

            #Choose a Movie
            else:
                info()




#Allow the user to select filters
def filters():

    #Global Variables
    global ageFilter
    global minlengthFilter
    global maxlengthFilter
    global movieratingFilter
    global genreFilter
    global directorFilter
    global repeat

    #Loop the menu so that the user can select all of the filters that they want
    while True:

        #Show the filters that have already been selected
        print("\n")
        print("Selected Filters:")
        if ageFilter != 1000:
            print(f"Age: {ageFilter} years")
        if minlengthFilter != 0:
            print(f"Minimum Length: {minlengthFilter} minutes")
        if maxlengthFilter != 1000:
            print(f"Maximum Length: {maxlengthFilter} minutes")
        if movieratingFilter != -1:
            print(f"Rating: At least {movieratingFilter}")
        if genreFilter != "":
            print(f"Genre: {genreFilter}")
        if directorFilter != "":
            print(f"Director: {directorFilter}")


        #Show the user which options they have
        print("\nFilters:")
        print("1. Age")
        print("2. Min Length")
        print("3. Max Length")
        print("4. Rating")
        print("5. Genre")
        print("6. Director")
        print("\n9. Search")
        print("0. End")

        #Collect input from the user
        action = input("\nSelect a filter: ")

        #Filter age
        if action == "1":
            ageFilter = int(input("What is the max age you are looking for?: "))

        #Filter minimum length
        elif action == "2":
            minlengthFilter = int(input("What is the minimum length you are looking for? (minutes): "))

        #Filter maximum length
        elif action == "3":
            maxlengthFilter = int(input("What is the maximum length you are looking for? (minutes): "))

        #Filter minimum rating
        elif action == "4":
            movieratingFilter = float(input("What is the minimum rating you are interested in? (0 - 10): "))

        #Filter genre
        elif action == "5":
            genreFilter = input("What genre are you interested in?: ").title()

        #Filer director
        elif action == "6":
            directorFilter = input("Which director do you want to see?: ").title()

        #Search
        elif action == "9":
            search(ageFilter, minlengthFilter, maxlengthFilter,
            movieratingFilter, genreFilter, directorFilter)
            break

        #End the program
        elif action == "0":
            repeat = False
            break

        #Invalid input
        else:
            print("\nInvalid input. Try again.")
            input("\nPress Enter to Continue")

def search(age, minlength, maxlength, movierating, genre, director):
    for i in range(len(titleData)):
        if ((2026 - int(yearData[i]) < age) and (int(timeData[i]) > minlength)
            and (int(timeData[i]) < maxlength) and (movierating <= ratingData[i])
            and (genre in genreData[i]) and (director in directorData[i])):
            filter.append(i)


#Present the info about a movie that the user selects
def info():
    global repeat

    print("\nThese are the top movies for you:")
    for i in range(len(filter)):
        number = i + 1
        print(f"{number}. {titleData[filter[i]]}")

    #Find out which movie the user is interested in
    action = input("\nWhich movie do you want to learn more about?: ")

    #Check if the user put in a valid input
    if int(action)-1 >= len(filter) or int(action) <= 0:
        print("\nMovie not in list. Please try again.\n")
        input("Press Enter to Continue")
        filter.clear()

    #Give info about the selected movie
    else:
        #Title
        print(f"\nSelected Movie: {titleData[filter[int(action)-1]]}")

        #Release Year
        print(f"Release Year: {yearData[filter[int(action)-1]]}")

        #Duration
        print(f"Runtime: {timeData[filter[int(action)-1]]} minutes")

        #Genre
        print(f"Genre: {genreData[filter[int(action)-1]]}")

        #Rating
        print(f"Rating: {ratingData[filter[int(action)-1]]}")

        #Director
        print(f"Director: {directorData[filter[int(action)-1]]}")

        #Actors
        print(f"Staring: {star1Data[filter[int(action)-1]]}, {star2Data[filter[int(action)-1]]}, {star3Data[filter[int(action)-1]]}, {star4Data[filter[int(action)-1]]}")

        #Movie Overview
        print(f"Overview: {overviewData[filter[int(action)-1]]}")

        repeat = input("\nPress 1 to search again or 0 to end: ")
        if repeat == "0":
            #End Program
            repeat = False
            print(f"\nThank you for using Movie Picker! Enjoy {titleData[filter[int(action)-1]]}!\n")
        else:
            repeat = True
            filter.clear()

#Main
main()


#Sources

#All of the data in this program comes from IMDB Top 1000 movies and TV shows
#Dataset shared by code.org
#https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc

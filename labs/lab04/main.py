# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# CS 31 Isabella Garcia 10/29/26
import random

def display_title():
    print("Guess the number!")
    print()

def get_name():
    player_name = input("What is your name? ")
    print("Hello", player_name)
    print()

def play_game(wins):
    level = input("What game level would you like to play? E for Easy, M for Medium, or H for Hard! ")#have to make sure it's input so the player can input an answer, almost just put print lol
    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 11
        tries = 8
    elif level.lower() == "h":
        max_number = 1000
        tries = 10
    else:
        print("Sorry. Invalid input. Please try again. ")




    number = random.randint(1, max_number) #made LIMIT to max number when incorporating new levels with new maxes
    print("I'm thinking of a number from 1 to " + str(max_number) + "\n")
    count = 1
    while count <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries. \n")
            wins += 1 #will increase every time the player wins a round
            print ("You have won ", wins, "games.")
            return wins
    else:
        print("Sorry. You ran out of guesses. The number was", number)
def main():
    display_title()
    get_name()
    wins = 0
    again = "y"
    while again.lower() == "y":
        wins = play_game(wins) #to make sure that the wins keep stacking (ex, win two times it will say 2 games won)
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
    

    
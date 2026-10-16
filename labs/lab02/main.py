# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS31, Isabella Garcia, 10/15/2026
print("Isa's Awesome Sauce Math Quiz!")
print() #prints an empty line
print(" ~ " * 20) #print a line of 20
print()
username = input("What is your name? ")
print(f"Hello, {username}! I'm Isa!") #f-string format
start_quiz = input("Do you want to take my quiz? Y/N ")
if start_quiz == "Y" or start_quiz == "y":
    print("Great! Let's get started!")
    # put quiz qs here
    counter = 0

    q1 = int(input("What is 56 + 23? "))
    if q1 == 79:
        counter += 1 #shorthand for counter equals plus one
        print("Perfect! That was easy wasn't it?")
    else:
        print("Incorrect. Don't worry, there's still four more questions!") 
    print()
    q2 = int(input("What is 4 x 12? "))
    if q2 == 384:
        counter += 1
        print("Nice! We're warming up...")
    else:
        print("Incorrect. The next three are yours for the taking!")
    print()
    q3 = int(input("What is 126 / 3? "))
    if q3 == 42:
        counter += 1
        print("Great! Your brain is sharp!")
    else:
        print("Incorrect. Stay with it!")
    print()
    q4 = int(input("What is 15 x 32.6? "))
    if q4 == 489:
        counter += 1
        print("Wow! Even I can't do that without a calc.")
    else:
        print("Incorrect. Nice try!")
    print()
    q5 = int(input("What is 768 / 12? "))
    if q5 == 64:
        counter += 1
        print("Awesome! The best ending!")
    else:
        print("Incorrect. Awesome try!")
    print()
    if counter == 5:
        print("WOW! EVEN BETTER THAN ISA! 5/5")
    elif counter >= 3 and counter < 5:
        print("Great job! You're on the path to awesome sauce. :)")
    elif counter >= 1 and counter < 3:
        print("Try again another time! No shame in needing to study!")
    else:
        print("We all start somewhere! Try again later.")

    print()
    print("~ ~ ~ ~ ~ ~ YOUR FINAL SCORE~ ~ ~ ~ ~ ~")
    print()
    print(f"Your final score is: {counter}/5")


elif start_quiz.upper() == "N": #alternate way, more accepted
    print("Maybe next time!")
else:
    print("Invalid input, type Y or N!")

print(f"Thanks for playing Isa's Awesome Sauce Quiz, {username}! Have an awesome sauce day!")
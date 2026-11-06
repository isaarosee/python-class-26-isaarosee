# module file for lab 5 - nameformat.py
def hello_world():
    print("Hello Halloween 2026!")

def sayHello(firstName):
    """Definition: A simple function that takes a firstName input and says hello to that name""" #""" used to create documentation
    print(f"Hello there {firstName}. What a day it is to live!") #f used for string function
    print()


def fullName(firstName, lastName):
    """Definition: A simple function that takes a firstName and lastName input and outputs the full name"""
    print(f"{firstName} {lastName}")
    print()

def lastNameFirst(firstName, lastName):
    """Definition: A simple function that takes a firstName and lastName input and outputs the last and first name with a comma"""
    print(f"{lastName}, {firstName}")
    print()


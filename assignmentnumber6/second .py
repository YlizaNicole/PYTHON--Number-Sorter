#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random
import math
def intro ():
    print ("Hello User! this a addition quiz game")
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, welcome again to this program! enter your answer. Good Luck! """. format(name))
    quest = input ("are you ready? yes or no: ")
    if quest == "yes": 
        print ("Let's play!")
    else:
        print ("that's okay, no pressure! i'll give the first number and there's no time limit!")


def infos ():
    score= 0
    
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1 + number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")


    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")
    
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")

    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")

    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        score = score +1
        print("Correct! :)")
    else: 
        print("Incorrect :(")
    
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1 + number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")


    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :) ")
        score = score +1
    else: 
        print("Incorrect :(")
    
    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")

    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        print("Correct! :)")
        score = score +1
    else: 
        print("Incorrect :(")

    number1 = random.randint(0,99)
    number2 = random.randint(0,99)
    total = number1+number2
    print(number1,"+",number2, end= "")
    answer1 = int(input("="))
    if answer1 == total : 
        score = score +1
        print("Correct!:)")
    else: 
        print("Incorrect :(")

    print("Your total score is " + str(score) + " out of 10")
    
def goodbye ():
    print ("thank you for playing!")

intro ()
infos ()
goodbye ()

name=input("hello what is your name?\n")

print("hello " + name + " i am guessing a number in range 1 to 20")
print("you only have 5 chances to guess the number")

import random

secret_number=random.randint(1,20)


for guess_iteration in range(1,6):
    try:
        guess=int(input())
        if guess<secret_number:
            print("you guess number is too low")
        elif guess>secret_number:
            print("you guess number is too high")

        else:
            #guess==secret_number
            break
    except ValueError:
        if guess_iteration!=5:
            print("please dont mess with me enter a numeric number")


try:
    if guess==secret_number:
        print("you won "+" in  "+ str(guess_iteration)+" iterations")

    else:
        print("game over")
except:
    print("you did not enter numeric value you lose")

    
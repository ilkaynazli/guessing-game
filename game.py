"""A number-guessing game."""

# Put your code here
print ('Hello Player!')
name = input("What's your name : ").title()
print("Welcome {} to the number guessing Game ".format(name))

import random

secret_number = random.randint(1,100)
guessed_count = 0

while True:
    guessed_count+=1
    guess = int(input("Enter your guess "))
    if guess == secret_number:
        print("Yay, You Guessed Correct")
        break
    elif guess < secret_number:
        print("guess is too low")
    else:
        print("guess is too high")
    

print ("You have guessed {} times" .format(guessed_count))
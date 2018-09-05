"""A number-guessing game."""

# Put your code here
print ('hi player!')
name = input("What's your name : ")
print(name)

import random

secret_number = random.randint(1,100)
guessed_count = 0

while True:
    guessed_count+=1
    guess = int(input("Enter your guess "))
    if guess == secret_number:
        print("Yay")
        break
    elif guess < secret_number:
        print("guess is too low")
    else:
        print("guess is too high")
    

print ("you have guessed {} times" .format(guessed_count))
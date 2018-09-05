"""A number-guessing game."""


# Put your code here
import random
print ('Hello Player!')
name = input("What's your name : ").title()
print("Welcome {} to the number guessing Game ".format(name))



secret_number = random.randint(1,100)
guessed_count = 0

while True:
    
    try:    
        guess = int(input("Enter your guess "))
    except:
        print ("That is not an integer!")
        continue

    if guess < 1 or guess > 100:
        print ('your guess is out of range')
        continue
    guessed_count+=1
    if guess == secret_number:
        print("Yay, You Guessed Correct")
        break
    elif guess < secret_number:
        print("guess is too low")
    else:
        print("guess is too high")
    

print ("You have guessed {} times" .format(guessed_count))
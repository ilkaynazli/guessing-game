"""A number-guessing game."""


# Put your code here
import random
print ('Hello Player!')
name = input("What's your name : ").title()
print("Welcome {} to the number guessing Game ".format(name))


def guess_the_number():
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

guess_the_number()

def choice():
    while True:
        choice_user = input("Would you like to play again? ").lower()
        if choice_user == 'y':
            guess_the_number()
        else:
            print('thank you for playing.')
            break

choice()

# while True:
#     choice_user = input("Would you like to play again? Y or N: ")
#     if choice_user == 'N':
#         print ('It was fun to play. See you again later.')
#         break
#     else:
#         guess_the_number()
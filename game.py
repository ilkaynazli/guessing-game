"""A number-guessing game."""


# Put your code here
import random
print ('Hello Player!')
name = input("What's your name : ").title()
print("Welcome {} to the number guessing Game ".format(name))


def guess_the_number():
    secret_number = random.randint(1,100)
    guessed_count = 0
    best_score = 100

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
    if guessed_count < best_score:
        best_score = guessed_count
    return best_score


best_score = guess_the_number()



def choice():
    while True:
        choice_user = input("Would you like to play again? Y or N:").lower()
        if choice_user == 'y':
            guess_the_number()
        else:
            print('It was fun to play. See you again later')
            print("Your Best Score was {}".format(best_score))
            break

choice()

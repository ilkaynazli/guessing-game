"""A number-guessing game."""


# Put your code here
import random
print ('Hello Player!')
name = input("What's your name? ").title()
print("Welcome {} to the number guessing game ".format(name))

def get_range():
    print ("Let's find out our range for the game.")
    low_limit = int(input("Please enter the lower limit: "))
    high_limit = int(input("Please enter the higher limit: "))
    range_of_game = high_limit - low_limit
    return (low_limit, high_limi, range_of_game)

def guess_the_number():
    (low, high, best_score) = get_range()
    secret_number = random.randint(low, high)
    guessed_count = 0
    limit = 15
    
    while True:

        try:    
            guess = int(input("Enter your guess "))
        except:
            print ("That is not an integer!")
            continue

        if guess < low or guess > high:
            print ('Your guess is out of range')
            continue
        guessed_count+=1
        if guessed_count >= limit:
            print ('You have guessed too many times. The game is over.')
            break
        if guess == secret_number:
            print("Yay, your guess is correct! Congratulations!")
            break
        elif guess < secret_number:
            print("Guess is too low.")
        else:
            print("Guess is too high.")
        

    print ("You have guessed {} times" .format(guessed_count))
    if guessed_count < best_score:
        best_score = guessed_count
    return best_score


best_score = guess_the_number()



def choice():
    while True:
        choice_user = input("Would you like to play again? Y or N:").lower()
        if choice_user == 'y' or choice_user == 'yes':
            best_score = guess_the_number()
        else:
            print('It was fun to play. See you again later')
            print("Your Best Score was {}".format(best_score))
            break

choice()

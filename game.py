"""A number-guessing game."""


# Put your code here
import random


def get_range():
    print ("Let's find out our range for the game.")
    low_limit = int(input("Please enter the lower limit: "))
    high_limit = int(input("Please enter the higher limit: "))
    return (low_limit, high_limit)

def guess_the_number(points):
    (low, high) = get_range()
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
            points.append(guessed_count*(high-low))
            break
        elif guess < secret_number:
            print("Guess is too low.")
        else:
            print("Guess is too high.")
        

    print ("You have guessed {} times" .format(guessed_count))
    
    return guessed_count

def computer_guesses_the_number():
    (low,high) = get_range()
    print ("Please select a number and I will try to guess it.")
    print ("Don't tell me until I guess it correctly.")
    while True:
        guess = random.randint(low,high)
        print ("I have guessed {}." .format(guess))
        user_input = input("Is this high or low? ").lower()
        if user_input == 'high':
            high = guess
        elif user_input == 'low':
            low = guess 
        else:
            print ("Your number was {}! I won!" .format(guess))
            break

def player_guesses_the_number():
    points = []
    best_score = guess_the_number(points)
    
    while True:
        choice_user = input("Would you like to play again? Y or N:").lower()
        if choice_user == 'y' or choice_user == 'yes':
            score = guess_the_number(points)
            if score < best_score:
                best_score = score

        else:
            print('It was fun to play. See you again later')
            print("Your Best Score was {}".format(best_score))
            print (points)
            break

def main():
    
    print ('Hello Player!')
    name = input("What's your name? ").title()
    print("Welcome {} to the number guessing game ".format(name))
    
    print("We can play 2 different games: I can guess or you can guess.")
    player = input('Would you like me to guess? If so press Y: ').lower()
    if player == 'y' or player == 'yes':
        computer_guesses_the_number()
    else:
        player_guesses_the_number()
    

main()

from random import randint
from sys import maxint

player_name = raw_input('What is your name? ')
print "Hi %s!" % player_name # greet the player by their name

low_score = maxint
while True:
    rand_num = randint(1, 100)
    print 'Hello, welcome to the guessing game!'

    num_of_guesses = 1
    guess = 101
    print rand_num 
    while True:
        try:
            guess = int(raw_input('Guess a number? '))
            if guess >= 1 and guess <= 100:
                if guess < rand_num:
                    print "Your guess is too low, try again."
                    num_of_guesses += 1
                elif guess > rand_num:
                    print "Your guess is too high, try again."
                    num_of_guesses += 1
                else:
                    print "number of guesses: %i" % num_of_guesses
                    print "low score is originally: %i" % low_score
                    if num_of_guesses < low_score:
                        low_score = num_of_guesses
                        print "low score is now: %i" % low_score 
                    print "You guessed the right number! You found my number in %i tries" % (num_of_guesses)
                    print "Would you like to play again? y/n"
                    answer = raw_input().lower()
                    if answer == "n":
                        break
                    elif answer == "y":
                        break

                    else:
                        while answer != "y" and answer != "n":
                            print "Not a valid answer!"
                            print "Please enter y or n"
                            answer = raw_input("> ")
            else:
                print "Oops, your guess was not between 1 and 100"
                continue
        except ValueError:
            print "Opps! That was not a number. Try again"
            continue
    if answer == "n":
        print "Your best score was %i" % (low_score)
        break        

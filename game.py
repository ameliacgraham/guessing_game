from random import randint

player_name = raw_input('What is your name? ')
print "Hi %s!" % player_name # greet the player by their name

while True:
    rand_num = randint(1, 101)

    print 'Hello, welcome to the guessing game!'

    guesses = 0
    guess = 101
    print rand_num 
    while True:
        try:
            guess = int(raw_input('Guess a number? '))
            if guess >= 1 and guess <= 100:
                if guess < rand_num:
                    print "Your guess is too low, try again."
                    guesses += 1
                elif guess > rand_num:
                    print "Your guess is too high, try again."
                    guesses += 1
                else:
                    print "You guessed the right number! You found my number in %i tries" % (guesses)
                    print "Would you like to play again? y/n"
                    answer = raw_input()
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
        break        

from random import randint

rand_num = randint(1, 101) 

print 'Hello, welcome to the guessing game!'
player_name = raw_input('What is your name? ')
print "Hi %s!" % player_name # greet the player by their name

guesses = 0
guess = 101
while True:
    while True:
        try:
            guess = int(raw_input('Guess a number? '))
            break
        except ValueError:
            print "Opps! That was not a number. Try again"
            continue

        if guess >= 1 and guess <= 100:
            if guess < rand_num:
                print "Your guess is too low, try again."
                guesses += 1
            elif guess > rand_num:
                print "Your guess is too high, try again."
                guesses += 1
            else:
                print "You guessed the right number! You found my number in %i tries" % (guesses)
                break
        else:
            print "Oops, your guess was not between 1 and 100"
            continue  
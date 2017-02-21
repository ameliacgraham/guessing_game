from random import randint

rand_num = randint(1, 101) 

print 'Hello, welcome to the guessing game!'
player_name = raw_input('What is your name? ')
print "Hi %s!" % player_name # greet the player by their name

guesses = 0
guess = 101
while True:
    guess = int(raw_input('Guess a number? '))
    if guess < rand_num:
        print "Your guess is too low, try again."
        guesses += 1
    elif guess > rand_num:
        print "Your guess is too high, try again."
        guesses += 1
    else:
        print "You guessed the right number! You found my number in %i tries" % (guesses)
        break

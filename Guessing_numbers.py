#Ask the user to guess the random number.
#If he guess in 3 tries then he will win otherwise he will lose/.

import random

secret_number = random.randint(1, 5)

guess = int(input("....Hey there! Lets play a guessing Game....\n\nEnter a number between 1 and 5: "))
count = 0
limit = 2
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if count < limit and guess < secret_number:
        guess = int(input("Your guess is wrong. Try again.\nEnter number: "))
        count += 1
    elif guess > secret_number:
        guess = int(input("Your guess is wrong. Try again. \nEnter number: "))
        count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Your guess is wrong.  You lose\nBetter Luck next time")
else:
    print("Your guess is right! You Win")
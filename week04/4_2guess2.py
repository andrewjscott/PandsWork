# Promts the user to guess a number and requests them to keep guessing until they get the correct number
# Gives feedback whether the user's guess is too high or too low
# Author: Andrew Scott

# Defines a variable with a number for the user to guess
numToGuess = 50

# A variable that contains the value entered as the user's guess
guess = int(input("Guess the number: "))

# A loop that tells the user their guess is wrong when their guessed number is not equal to the initial number and continues to
# ask them to guess again
# The if statement lets the user know if their guess is lower than the initial number, otherwise it tells them it is too high
while guess != numToGuess:
    if guess < numToGuess:
        print("Wrong! Too low!")
    else:
        print("Wrong! Too high!")
    guess = int(input("Please guess again: "))

# The previous loop ends when the number is correctly guessed and the variable guess is equal to numToGuess which leads to 
# a string being printed that tells the user that they are correct
print("Yes! That is correct! The number is " + str(numToGuess) + ".")
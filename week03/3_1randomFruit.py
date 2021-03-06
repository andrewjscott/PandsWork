# Prints out a random fruit from a predefined list of fruits
# Author: Andrew Scott

# Imports the random module
import random

fruits = ['apple', 'banana', 'orange', 'pear']

# Each string in the list is assigned a numberical position in the list. 0 is the start, while -1 is the end of the list
# This picks a random number that corresponds to the string in the position of the randomly selected number and 
# assigns it to a variable
index = random.randint(0,len(fruits)-1)

# Takes the string in the randomly selected position and assigns it to a new variable
fruit = fruits[index]

# Outputs the random fruit
print("A random fruit: {}".format(fruit))
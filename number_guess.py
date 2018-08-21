'''This program does the following
Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).'''
'''This program does the following
Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).'''
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum posssible value = %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Please select a number less than %d" % max_val
  else:
    print "Rolling..." 
    sleep(2) # to simulate the dice rolling for 2 seconds
    print "First Roll = %d" % first_roll
    sleep(1)
    print "Second Roll = %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total roll = %d" % total_roll
    print "Result..."    
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
      print "Computer won!"    
roll_dice(6)
#importing randomness module
from random import randint
#importing from system-python the exit module
from sys import exit
#importing delay time module
import time
#allows this program to use string values
import sys,string
#Printing out the function of this program
print "\t***Dice Roll Simulator***\n \n"

#function definition/ protocols

#function to roll the Dice
def roll():
    print "\nRolling The Dice...\n"
    #wait for 1 second (arouse anticipation)
    time.sleep(1)
    #print random integer where {x|1<=x<=6}
    print randint(1,6)

#do you want to roll it again function
def again():
    choice = raw_input("\nDo You Want to Roll Your Dice Again? [y/n] :")
    #if what the user typed is either y or Y, roll the dice again
    if choice == 'y':
        roll()

    #if what the user typed is either n or N, exit the program
    elif choice == 'n':
        print "\nExiting the Program...\n\nThank you! \n\n Bye!"
        #wait 1 second
        time.sleep(1)
        #exit the program
        sys.exit()

    #if input values != {'n','N','y','Y'}, ask his/her choice again
    else:
        print "\nInvalid Choice. Please Respond with either 'y' or 'n'...\n Try Again! \n"


#function re-call

roll()

#while the choice is neither 'y' nor 'n' run function(again) repeatedly until it reaches sys.exit()
while again != 'y' and 'n':
        again()

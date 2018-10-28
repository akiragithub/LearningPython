# -*- coding:latin-1 -*
# OpenClassrooms ZCasino TP for validating the Part 1 of the book
# Coded by Suxess this 27/10/2018
from random import randrange
from math import ceil
def main():
    name = get_name()
    initial_bet = get_bet()
    name = 'Suxess'
    initial_bet = 99
    gain = initial_bet
    while 0 < gain :
        gain = play(name,gain)
    print("The game is over, I always win !")

def play(name,gain):
    maxi_selectable_value = 49
    choice = get_choice(name)
    choice = 46
    system_output = randrange(maxi_selectable_value)
    gain = computize_gain(choice,system_output,gain)
    if 0 < gain :
        print(name," ! You are as lucky as Lucky Luke, the game continues !\n")
        print("You have now have ",gain," in the system")
        print ("Let's play one more time")
        print("======================================================")
    return gain

def get_name():
    return input("Hello ! I am ZCasino, your python virtual casino\nMay I know you ?\n Your name : ")
def get_bet():
    bet = input("How much US Dollars are you betting ?\n")
    try :
        bet = int(bet)
    except ValueError :
        Print("You can only bet positive integers")
        get_bet()
    return bet
def get_choice(name):    
    choice = input("Choose a number from 0 to 49 : ")
    try :
        choice = int(choice)
        assert (0<=choice<=49)
    except ValueError :
        print(name,"! If you want to play you have to follow the rules !")
        get_choice(name)
    except AssertionError :
        print ("Assert error; choose a number between 0 and 49!\n")
        get_choice(name)
    return choice

def computize_gain(choice,system_output,gain):
    
    if choice == system_output :
        gain = 3*gain
    elif ceil(choice-system_output)%2 == 0 :
        #If both numbers have the same parity
        #User gains half of the initial amount in the system at this time
        print("Same Parity")
        gain = gain/2
        if gain%2 !=0 :
            print("gain%2 = ",gain%2," and gain value is ",gain)
            gain = int(gain+1)
    else :
        print("Different Parities")
        gain = 0
    # for all the other cases he losts all his money; so we let the default gain as if
    print("You choosed : ",choice)
    print("The System choosed : ",system_output)
    print("Gain is : ",gain)
    return gain
        
if __name__=="__main__" :
    main()

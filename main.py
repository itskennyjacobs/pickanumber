import os
import time
import random

# "Pick a Number" is a text based game. You pick a number 1-9 and place a bet.

# Your starting balance and global variable to store current balance
balance = 1000000

# global variable to store the current bet amount
bet = None

# global variable to store the current winning number
winning_number = None

# global variable to store the current number picked
pick = None

# Be sure to change this to False when you are ready to play!
# While debug is true, it will show you the winning number while on the pick_number screen.
# This will allow you to test winning/losing outcomes
debug = True

# global variable to store the current game message
message = "Good luck!"


# This function displays when you have debug set to True
def display_debug_info():
    if debug:
        print(f"Balance: {balance}  |  Winning Number: {winning_number}  |  Pick: {pick}  |  Bet: {bet}\n\n\n")


def display_header():
    os.system('cls')
    display_debug_info()
    print("<<<<< Pick a Number! >>>>>\n\n")
    time.sleep(.1)
    print(f"Balance: {balance}\n")
    print(f"Message: {message}")
    print("\n\n\n\n")


def display_welcome():
    display_header()
    print(f"Welcome to Pick a Number! Place a bet and pick a number 1-9!\n\n")
    action = input("Are you ready?\n\n(P)lay or (Q)uit:  ")
    if action == 'p':
        place_bet()
    elif action == 'q':
        quit()
    else:
        print("You've entered an invalid option, please try again.")
        time.sleep(.1)
        os.system('cls')
        display_welcome()


def display_game_menu():
    display_header()
    action = input("(P)lay again or (Q)uit:  ")
    if action == 'p':
        place_bet()
    elif action == 'q':
        quit()
    else:
        print("You've entered an invalid option, please try again.")
        time.sleep(.1)
        os.system('cls')


def place_bet():
    display_header()
    global bet
    global message
    message = "Good luck!"
    bet = int(input(f"How much would you like to bet? (1 -  {balance})  "))
    generate_number()
    pick_number()


def generate_number():
    global winning_number
    winning_number = random.choice(range(1, 9))


def pick_number():
    display_header()
    global pick
    global message
    message = "Good luck!"
    pick = int(input("Pick a number between 1 and 9:  "))
    play_round()


def increase_balance(amount_won):
    global balance
    balance = balance + amount_won


def decrease_balance(amount_lost):
    global balance
    balance = balance - amount_lost


def play_round():
    global message
    if pick == winning_number:
        increase_balance(bet)
        message = f"You won ${bet}!"
    else:
        decrease_balance(bet)
        message = f"You lost ${bet}! You picked {pick} and the winning number was {winning_number}."
    display_game_menu()


if __name__ == '__main__':
    display_welcome()

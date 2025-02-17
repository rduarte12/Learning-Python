""" 
 This code is for detection if a credit card number is valid or not
 and also to determine the type of credit card
 This code is an adaptation of the exercise "credit" from CS50x, Harvard University
 The original code was written in C, and I adapted it to Python

"""

# Code by Rafael Duarte

# Import the functions from the other files
from algorithm import algorithm
from card_type import card_type

# Recive input from user, a credit card number only positive numbers
while True:
    try:
        credit_card = int(input("Credit card number: "))

            # Verify if the input is a valid number (only positive numbers)
        if credit_card > 0: # If yes, break
            credit_card = str(credit_card)
            break

        else: # If not, ask for a valid number
            print("Please, enter a valid number")
            continue

    except ValueError as e: # If not, ask for a valid number
        print(f"Please, enter a valid number. {e} is not a number")
        continue
    
    
# Luhn's Algorithm and card type detection
if algorithm(credit_card) == False:
    print("INVALID")
    exit()
if algorithm(credit_card) == True:
    print(card_type(credit_card))
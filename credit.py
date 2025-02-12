# This code is for detection if a credit card number is valid or not
# and also to determine the type of credit card
# This code is an adaptation of the exercise "credit" from CS50x, Harvard University

# Code by Rafael Duarte

# Recive input from user, a credit card number only
    # Verify if the input is a valid number (only positive numbers)
    # If not, ask for a valid number
    # If yes, continue

# Convert the input into a list

# Check if the credit card number is valid (Luhn's Algorithm)
    # If not, print "INVALID"
    # If yes, continue

# Check the type of credit card
    # If the number starts with 4
        # If the number has 13 or 16 digits
        # If not, print "INVALID"
    # If the number starts with 34 or 37, print "AMEX"
        # If the number has 15 digits, print "AMEX"
        # If not, print "INVALID"
    # If the number starts with 51, 52, 53, 54 or 55, print "MASTERCARD"
        # If the number has 16 digits, print "MASTERCARD"
        # If not, print "INVALID"
    #If the number not fits in any of the above, print "INVALID"
def card_type(credit_card):
# Check the type of credit card
    credit_card = list(map(int, str(credit_card)))
    # If the number starts with 4 and has 13 or 16 digits, print "VISA"
    if credit_card[0] == 4 and (len(credit_card) == 13 or len(credit_card) == 16):
        return("VISA")
    # If the number starts with 34 or 37 and has 15 digits, print "AMEX"
    elif credit_card[0] == 3 and (credit_card[1] == 4 or credit_card[1] == 7) and len(credit_card) == 15:
        return("AMEX")
    # If the number starts with 51, 52, 53, 54 or 55 and has 16 digits, print "MASTERCARD"
    elif credit_card[0] == 5 and (credit_card[1] in range(1,6)) and len(credit_card) == 16:
        return("MASTERCARD")
    # If the number not fits in any of the above, print "INVALID"
    else:
        return("INVALID")

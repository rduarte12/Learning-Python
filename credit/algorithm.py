def algorithm(credit_card):
    # Convert the input into a reverse list
    credit_card = list(map(int, str(credit_card[:: -1])))

    # Check if the credit card number is valid (Luhn's Algorithm)
    lenght = len(credit_card)
    sum = 0
    flag = False

    for i in range(lenght):
        num = credit_card[i]

        if flag:
            num *= 2

            if num > 9:
                num -= 9
    
        sum += num
        flag = not flag
    
    if sum % 10 != 0: # If not, print "INVALID"
        return False
    
    else: # If yes, returne True
        return True
    
    

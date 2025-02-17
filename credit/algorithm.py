def algorithm(credit_card):

    """_summary_
    This code checks if a credit card number is valid or not,
    based on Luhn's Algorithm

    Returns:
        credit_card(str): The input of the credit card number
        in the code, the input is converted to a list of integers

        lenght(int): The lenght of the credit card number
        sum(int): The sum of the digits of the credit card number
        flag(bool): A flag to check if the number needs to be multiplied by 2
    """

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
    
    

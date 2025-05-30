print("This is a bank operator")


tax_limite = 0.3
balance, withdraw = 5000, float(input("Withdraw valor: "))
limite = balance * tax_limite
special_account = False

if (withdraw <= balance and withdraw <= limite) or (special_account and withdraw <= balance):
    print(f"You are able to withdraw the money: {withdraw}")
    print('Take the money on the box')
    print('Your balance is: ', balance - withdraw)
else:
    print(f"You aren't able to withdraw the money: {withdraw}")
    print('Your balance is: ', balance)
    print('You need more money to withdraw this valor')


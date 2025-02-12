#Here, I am register some logic operations
money = 1000
phone_price = 500
tax = 0.08
total_price = phone_price*(1+tax)

# I can buy the phone if I have enough money
if money >= total_price:
    print("I have enough money to buy the phone? ", total_price <= money)
    print("You can buy the phone, and rest money is: ", money - total_price)

# I can't buy the phone if I don't have enough money
else:
    print("I don't have enough money to buy the phone? ", total_price > money)
    print("You can't buy the phone, and you need more money: ", total_price - money)
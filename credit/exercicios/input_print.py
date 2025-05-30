# Description: This program takes user input and prints it out
name = input("What is your name? ")
age = input("How old are you? ")

print(f"My name is {name} and I am {age} years old")

# The print function has some parameters that can be used to change the output
print(name, age)
print(name, age, end="...\n")
print(name, age, sep="#")
print(name, age,  sep="#", end="...\n")

def cont():
    num = list(input("Enter a number: "))
    return num

verify_cont = cont();
print(verify_cont)
print(int(verify_cont[2]) - int(verify_cont[1]))

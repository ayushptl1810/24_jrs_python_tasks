#Q2: Take an input from the user the factorial of a number if the user enters a string print not a valid input
a = input("Enter a number: ")
fact = 1
if a.isalpha():
    print("Enter a valid integer")
else:
    num = int(a)
    while num != 0:
        fact = fact * num
        num -= 1
    print(fact)


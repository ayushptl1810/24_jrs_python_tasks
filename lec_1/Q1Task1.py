#Q1: Take an input from user is should be a number and find out how many digit it has
a = int(input("Enter a number: "))
count = 0
while a > 0:
    a = a // 10
    count += 1
print(count)

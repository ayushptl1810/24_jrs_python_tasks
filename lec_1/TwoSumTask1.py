def targetFind(list, target):
    for i in list:
        for j in list:
            if(i + j == target):
                return i,j
    return None


l = input("Enter comma seperated numbers: ").split(",")
list = []
for num in l:
    list.append(int(num))
target = int(input("Enter a target: "))
indice1, indice2 = targetFind(list,target)
print(indice1,indice2)
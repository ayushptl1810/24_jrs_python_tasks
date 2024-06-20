#Q3: Create a program

Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
# from this above data create a list brand,OS
#print(brand)
#['brand','hp','apple']
#print(os)
#['Windows','Linux','MAc-os']

brand = []
os = []
for laptop, key in Computers.items():
    brand.append(key["brand"])
    os.append(key["OS"])

# Print the lists
print(brand)
print(os)

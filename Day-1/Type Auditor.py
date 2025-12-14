x = input("Enter a value : ")
print(type(x)) 
try:
    y = float(x)
    print(type(y))

except:
    print("Invalid Value.")
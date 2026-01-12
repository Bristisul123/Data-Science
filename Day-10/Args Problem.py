def deco(func):
    def wrap():
        print("The sum is : ")
    return wrap

@deco
def add(a, b):
    return a + b

print(add(6,10))

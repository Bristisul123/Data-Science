class Wallet:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return Wallet(self.x + other.x)

    def show(self):
        print("The new value is :", self.x)

w1 = Wallet(100)
w2 = Wallet(200)
w3 = w1 + w2
w3.show()



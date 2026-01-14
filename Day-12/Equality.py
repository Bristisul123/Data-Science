class Wallet:
    def __init__(self,x):
        self.x = x
    def __eq__(self,other):
        return self.x == other.x

w1 = Wallet(100)
w2 = Wallet(200)
print(w1 == w2)



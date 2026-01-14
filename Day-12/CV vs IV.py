class Human:
    species = "Human"

    def __init__(self,name):
        self.name = name
    def show(self):
        print("The species is :  and it's name is : ",self.species,self.name)

a = Human("A")
a.species = "Dog"
a.show()

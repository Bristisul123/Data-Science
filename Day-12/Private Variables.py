class User:
    def __init__(self):
        self.__password = "Ira"   
   
    def show_pass(self):
        print("The password is : {}".format(self.__password))
    def set_password(self, new):
            self.__password = new

u = User()
u.show_pass()
u.__password = 123
u.show_pass()

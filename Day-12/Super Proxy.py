class User:
    def __init__(self,user):
        self.user = user

class admin(User):
    def __init__(self,user,password):
        super().__init__(user)
        self.password = password
         
    def admin_db(self):
        print("The admin name is :",self.user)


Admin = admin("Rian",123)
Admin.admin_db()
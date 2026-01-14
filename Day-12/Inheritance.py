class User:
    def __init__(self,user):
        self.user = user

class admin(User):
    def delete_db(self):
        print("Database has been deleted")


Admin = admin("Iran")
Admin.delete_db()
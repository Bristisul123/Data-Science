user = "admin"

def admin_required(func):
    def wrap():
        if user != "admin":
            raise PermissionError
        return func()
    return wrap

@admin_required
def db():
    print("Admin")

db()

user = "Admin"

def admin_required(func):
    def wrap():
        if user != "Admin":
            raise PermissionError
        return func()
    return wrap

@admin_required
def db():
    print("Admin")

db()

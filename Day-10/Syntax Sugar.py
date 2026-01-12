def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper

@decorator
def old_func():
    print("Hello")

old_func()
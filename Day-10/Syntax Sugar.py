def wrapper(func):
    def inner():
        print("Before Function")
        func()
        print("After Function")
    return inner
@wrapper
def old_func():
    print("Hi")

old_func()
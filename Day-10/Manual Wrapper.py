def wrapper(func):
    def inner():
        print("Before Function")
        func()
        print("After Function")
    return inner

def old_func():
    print("Hi")

new_func = wrapper(old_func)
new_func()
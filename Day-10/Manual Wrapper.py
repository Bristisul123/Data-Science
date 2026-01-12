def wrapper(func):
    def run_code():
        print("Before Function")
        func()
        print("After Function")

    return run_code

def old_func():
    print("Hello. My name is Bristi")


new_func = wrapper(old_func)
new_func()
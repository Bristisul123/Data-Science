import time

def timer(func):
    def wrap():
        start = time.time()
        func()
        end = time.time()
        print(f"The execution time is : {end-start}")
    return wrap

@timer
def work():
    time.sleep(1)

work()
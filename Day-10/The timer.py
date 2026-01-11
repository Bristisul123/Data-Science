import time

def timer(func):
    def wrap():
        start = time.time()
        func()
        print(start)
    return wrap

@timer
def work():
    time.sleep(1)

work()
def deco(func):
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)
    return wrap

@deco
def add(a, b):
    return a + b

print(add(6,10))

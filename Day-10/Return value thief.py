def bad_deco(func):
    def wrap(*args):
        func(*args)
    return wrap

@bad_deco
def test(a):
    return a

print(test(10))
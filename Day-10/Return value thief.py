def bad_deco(func):
    def wrap():
        func()
    return wrap

@bad_deco
def test():
    return 10

print(test())
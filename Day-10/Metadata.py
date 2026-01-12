def deco(func):
    def wrap():
        pass
    return wrap

@deco
def test():
    pass

print(test.__name__)

def repeat(times):
    def deco(func):
        def wrap():
            for _ in range(times):
                func()
        return wrap
    return deco

@repeat(3)
def text():
    print("Brainrot")

text()
def gen():
    list = []
    i = 1
    while i <= 100:
        yield i
        i += 1

print(next(gen()))
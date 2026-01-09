def gen1():
    for i in range(5):
        yield i

def gen2():
    for i in range(6,10,1):
        yield i

def main():
    yield from gen1()
    yield from gen2()

print(list(main()))
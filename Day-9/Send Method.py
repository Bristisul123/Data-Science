def gen():
    i = 1
    while True:
        value = yield i
        if value:
            i += value
        else:
            i += 1

x = gen()

for i in x:
    print(i)
    x.send(5)
    if i > 10:
        break
def run_avg():
    total, count = 0,0
    i = None
    while True:
        value = yield i
        total += value
        count += 1
        i = total / count


x = run_avg()
next(x)
print(x.send(5))
print(x.send(12))




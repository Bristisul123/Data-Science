def sqr(n):
    for i in range(n):
       yield i**2

def even(n):
    for i in n:
        if i % 2 == 0:
            yield i

x = even(sqr(15))
print(list(x))

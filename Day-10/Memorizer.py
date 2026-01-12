def cache(func):
    c = {}
    def wrapper(n):
        if n in c:
            return c[n]
        c[n] = func(n)
        return c[n]
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

print(fib(5))
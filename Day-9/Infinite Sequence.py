def fibo():
    i,j = 0,1
    while True:
        yield i
        i,j = j, i+j
        
x = fibo()       
for _ in range(10):
    print(next(x))


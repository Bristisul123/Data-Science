from functools import partial
def power(a,e):
     return a**e

square = partial(power,e=2)
print(square(8))
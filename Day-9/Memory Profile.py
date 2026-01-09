import sys
a = [x for x in range(1000)]
b= (x for x in range(1000))

print(sys.getsizeof(a))
print(sys.getsizeof(b))
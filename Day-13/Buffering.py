with open('buf.txt','w') as f:
    [f.write(str(i)+'\n') for i in range(5)]

with open('buf.txt') as f:
    print(f.readline())
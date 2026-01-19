n = [1,2,4,6,7,8]
t = 9
s = {}
for i in n :
    if t-i in s :
        print(i,t-i)
    s[i] = i
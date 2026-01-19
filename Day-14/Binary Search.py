def BS(s,t):
    l ,r= 0, len(s)-1
    while l <= r:
        mid = (r+l)//2
        if s[mid] == t:
            return mid
        elif s[mid] > t : 
             r = mid - 1
        else: l = mid + 1
    return -1

print(BS([2,4,6,8,9,11,12],11))
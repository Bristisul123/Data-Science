a = [1,2,5,7]
b = [3,6,9,12]
ml = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        ml.append(a[i])
        i +=1
    else :
        ml.append(b[j])
        j += 1

ml += a[i:] + b[j:]
print(ml)

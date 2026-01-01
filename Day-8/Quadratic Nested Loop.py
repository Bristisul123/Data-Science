def find_duplicate(listA,listB):
    matches = []
    for i in listA:
        for j in listB:
            if i == j:
                matches.append(i) 
    return matches

A = [1,2,3,4,5,6,7]
B = [2,4,6,8]
dup = find_duplicate(A,B)
print(dup)
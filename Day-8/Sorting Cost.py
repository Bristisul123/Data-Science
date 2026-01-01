def marge_sort(List):
    if len(List) <= 1:
        return List
    n = len(List)
    mid = n // 2
    left = marge_sort(List[0:mid])
    right = marge_sort(List[mid:])
    return merge(left,right)
 
def merge(l,r):
    new_list = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            new_list.append(l[i])
            i += 1
        else :
            new_list.append(r[j])
            j += 1

    new_list.extend(l[i:])
    new_list.extend(r[j:])
    return new_list

List = [2,6,3,9,8,4,5]
sort = marge_sort(List)
print(sort)


def insert_at_zero(List,target):
    n = len(List)
    List.append(None)
    for i in range(n,0,-1):
        List[i] = List[i-1]
    List[0] = target


List = [2,4,6,8,9,12]
add_value = insert_at_zero(List,2)
print(List)
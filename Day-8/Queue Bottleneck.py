def pop_from_zero(List):
    target = List[0]
    n = len(List)
    for i in range(n-1):
        List[i] = List[i+1]
    List.pop(n-1)


List = [2,4,6,8,9,12]
remove_value = pop_from_zero(List)
print(List)
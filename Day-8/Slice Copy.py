def slice_list(source,k):
    new_list = []
    for i in range(k):
        new_list.append(source[i])

    return new_list

List = [1,2,3,4,5]
# print(List[0:3])
sub = slice_list(List,3)
print(sub)
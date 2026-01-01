def build_dict(List):
    new_dict = [None]*len(List)
    for i in List:
        hash_val = hash(i) % len(new_dict)
        new_dict[hash_val] = i

    return new_dict


List = range(100)
print(build_dict(List))

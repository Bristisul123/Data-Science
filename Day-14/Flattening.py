def flat(l):
    s = []
    for i in l :
        if isinstance(i,list):
            s+=flat(i)
        else: s.append(i)

    return s
print(flat([1,[2,[3]]]))
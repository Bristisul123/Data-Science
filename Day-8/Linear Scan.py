def contains(List,target):
    i = 0
    length = len(List)

    while i < length:
        curr = List[i]
        if curr == target:
            return True
        i = i+1
    return False

List = list(range(-100,100000))
if contains(List,-5):
    print("-5 is Available")
else:
    print ("Not Available")


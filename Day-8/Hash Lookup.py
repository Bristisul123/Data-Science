def contains(List,target):
   hash_value = hash(target) % len(List)
   memory_slot = List[hash_value]

   if target in memory_slot:
    return True 
   else:
    return False


Set = [[] for i in range(1000)]

for i in range(-100, 1001):
    index = hash(i) % len(Set)
    Set[index].append(i)
print(contains(Set, -5))


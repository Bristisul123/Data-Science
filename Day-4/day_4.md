# Day 4 Lists (Data Structures)
## Theory: Mutability Memory 
Lists are Mutable. This means they can be changed in place. 
The Aliasing Trap: A = [1,2] B = A This does NOT copy the list. It creates a second name for the same list. Modifying B will destroy A. Solution: Always use B = A.copy(). 

```
data = [10, 20, 30, 40, 50]
# Slicing (Start : Stop : Step)
subset = data[1 : 4] #[20, 30, 40]
reverse = data[::-1] # [50, 40, 30, 20, 10]

# List Comprehension
# [Action for Item in List if condition]
squares = [x ** 2 for x in data]
print(squares)
```

# Goals:
1. Write b = a, you are copying the Reference (Memory Address), not the data.Fix: Use b = a.copy() or b = a[:] to force Python to allocate a new list in memory. 
2. Creates a Shallow Copy .Slicing syntax [start: stop: step]
3. Use .append() and .pop() as .append() and .pop() are optimized to O(1) time complexity and insert(0, x) is O(N).
4. Use of  List Comprehensions to avoiding the overhead .
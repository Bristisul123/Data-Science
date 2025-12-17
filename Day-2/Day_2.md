# Day 2 Logic Control Flow 
## Logic is the brain of your code. 
Truthiness: In Python, the following are considered False: 0, 0.0, "" (Empty String), [] (Empty List), None. Everything else is True. Short-Circuit Evaluation: if A and B: If A is False, Python never checks B. This is critical for preventing crashes (e.g., checking if a variable exists before accessing it). 

```
score = 85
# The Efficient Ladder
if score >= 0:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Temporary Operator (One-line logic)
status = "Pass" if score >= 70 else "Fail"
```

## Goal: 
1. Uses of Short-Circuit Evaluation.  
2. Write a script that checks if 0.1 0.2 == 0.3. Print the result (True/False). (Always use a tolerance threshold (epsilon) or round() when comparing floats in Data Science.)
3. Python objects have inherent Boolean values.
4. Using temporary variable to check atomic operation.


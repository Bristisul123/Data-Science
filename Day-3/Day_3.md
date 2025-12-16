# Day 3 Loops Iteration 
Loops allow us to automate tasks. 
- For Loops: Iterate over a known collection (List, String, Range).
- While Loops: Iterate as long as a condition (State) is True. 
Warning: While loops can run forever (Infinite Loop) if you don't write a line of code that changes the condition to False.

```
# The Infinite Input Pattern
while True:
    pwd = input("Set Password (min 5 chars): ")
    if len(pwd) >= 5:
        break  # Exits the loop
    print("Too Short. Try again.")

## Goal:
 1.  Use while True and handle the exit condition manually.
 2.  Calculate sum using a for loop and a tracker without using the math formula (n+1).
 3.  Use the continue keyword.
 4. Write a loop that prints every letter on a new line



    

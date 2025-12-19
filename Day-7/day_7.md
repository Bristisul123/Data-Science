#  Day 7 Error Handling (Exceptions) 
## Theory: Exception Bubbling
*When an error occurs, it "bubbles up" the call stack. If nothing catches it, the program crashes.*
**Defensive Programming:** *We use try/except blocks to catch these bubbles. This is required for Data Science pipelines where one bad row of data shouldn't stop a 10-hour training process.*
```
while True: 
    try: 
        val = int(input("Enter number: ")) 
        print (100 / val) 
        break 
    except ValueError: 
        print("Text is not allowed.") 
    except ZeroDivisionError:  
        print ("Cannot divide by zero.") 

```
## Goals:
1. Use try/except ValueError.The try block creates a "Safety Net" If a specific signal  hits the net.
2. Catch ZeroDivisionError. Catching this allows  data pipeline to  "Skipping bad row" instead of halting a 10-hour process. 
3. Use of finally block. Python ensures the finally code executes before leaving the scope.
4. Use of raise . It force python interpreter to stop normal execution and look for an exception handler (just like a built-in error).
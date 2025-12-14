total = int(input("Enter seconds : "))
hours = total // 3600
remaining = total % 3600
minute = remaining //60
second = remaining % 60

print(f"Hour : {hours} , Minutes : {minute} and  Seconds : {second}")
num = int(input("Enter a number : "))

if num < 0:
    raise ValueError("No negatives")
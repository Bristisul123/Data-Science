while True:
    try:
        age = int(input("Enter your age : "))
        print(f"You are {age} old")
        break
    except:
        print("Numbers Only")
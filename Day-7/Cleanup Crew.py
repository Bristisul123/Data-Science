while True:
    try:
        val1 = int(input("Enter the 1st value : "))
        val2 = int(input("Enter the 2nd value : "))
        print(val1 / val2)
    except:
        print("Numbers Only")
    finally:
       print("Execution Complete")
       break
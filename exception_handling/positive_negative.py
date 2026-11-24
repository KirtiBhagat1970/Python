try:
    num=int(input("Enter a number:"))
    if num<0:
        raise ValueError("Number is negative please enter a positive number")
    print("Number is positive")
except ValueError as e:
    print("Error:",e)
finally:
    print("Program executed successfully")
    
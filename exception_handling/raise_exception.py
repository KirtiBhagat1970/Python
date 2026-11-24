try:
    age=int(input("Enter a age:"))
    if age< 18:
        raise ValueError("you are not eligible to vote")
    print("you are eligible to vote")
except ValueError as e:
    print("Error:",e)
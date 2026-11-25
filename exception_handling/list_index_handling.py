try:
    index=int(input("Enter a index"))
    arr=[10,20,30,40,50]
    print("value:",arr[index])

except IndexError:
    print("user entered index is out of range")

except ValueError:
    print("please enter valid integer")

finally:
    print("Program Executed")
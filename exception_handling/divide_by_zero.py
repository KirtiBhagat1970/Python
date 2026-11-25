try:
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    
    result=num1/num2
    print("result:",result)
except ZeroDivisionError:
    print("Number cannot divide by zero")
except ValueError:
    print("please enter numbers only")
finally:
    print("division of two numbers done")
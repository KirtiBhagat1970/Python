try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    
    print("addition:",num1+num2)
    print("substraction:",num1-num2)
    print("multiplication:",num1*num2)
    print("division:",num1/num2)
except ZeroDivisionError:
    print("number cannot divide by zero")

except ValueError:
    print("please enter valid integer")

finally:
    print("Calculation completed")
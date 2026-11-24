try:
    num=int(input("Enter a number:"))
    result=[]
    
    for i in range(1,9):
        result.append(num//i)
    print(result)
    
except ZeroDivisionError as e:
    print("Error:",e)
    
except ValueError as e:
    print("Error:",e)
    
except IndexError as e:
    print("Error:",e)

finally:
    print("division of number by every element in range")
    

        
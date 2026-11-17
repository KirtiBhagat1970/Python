from calculator.addition import addition
from calculator.substraction import substraction
from calculator.multiplication import multiplication
from calculator.division import division
# from calculator.modulus import modulus

num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))

print("adition:",addition(num1,num2))
print("substraction:",substraction(num1,num2))
print("multiplication :",multiplication (num1,num2))
print("division:",division(num1,num2))
# print("modulus:",modulus(num1,num2))


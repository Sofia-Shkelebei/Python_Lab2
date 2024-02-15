# a) Write a program to add 2 numbers.
print("Program to add two numbers")
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = float(number1) + float(number2)
print("Sum:", sum)
print()

# b) Write a program to swap 2 variable values
print("Program to swap 2 variables values")
var1 = input("Enter the first value: ")
var2 = input("Enter the second value: ")
temp = var1
var1 = var2
var2 = temp
print("First variable:", var1)
print("Second variable:", var2)

# c) Write a Python program to compute the perimeter and area of a rectangle
Length = input("Enter the length of the rectangle: ")
Width = input("Enter the width of the rectangle: ")
Perimeter = 2*(float(Length) + float(Width))
Area = float(Length) * float(Width)
print("Perimeter:", Perimeter)
print("Area:", Area)


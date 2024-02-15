import math

# a) Write a program to find the circumference and area of a circle
Radius = float(input("Enter radius of the circle: "))
Area = math.pi * Radius**2
Circumference = 2*math.pi * Radius
print("The area:", Area, "\nThe circumference:", Circumference)

# b) Write a program that converts temperatures from Fahrenheit to Celsius
Temperature_in_Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
Temperature_in_Celsius = 5/9*(Temperature_in_Fahrenheit-32)
print("The temperature in Celsius:", Temperature_in_Celsius)

# c) Write a program to solve a given quadratic equation. e.g. a = 1, b = 3, c = 4
a = 1
b = 3
c = 4
Discriminant = b**2 - 4*a*c
x1 = (-b + Discriminant**0.5)/2*a
x2 = (-b - Discriminant**0.5)/2*a
print("The first root:", x1, "\nThe second root:", x2)

# d) Write a program to determine the compound interest.
Principal = 5000
APR = 3
Amount = Principal * (1 + APR/100)**10
print("The Amount:", Amount)







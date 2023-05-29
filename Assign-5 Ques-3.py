# Import math module for square root function
import math

# Get the sides of the triangle from the user
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check if the combination of sides is possible
if a + b > c and b + c > a and c + a > b:
  # Calculate the semi-perimeter
  s = (a + b + c) / 2

  # Calculate the area using Heron's formula
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))

  # Print the area
  print("The area of the triangle is", round(area, 2))
else:
  # Print an error message
  print("The combination of sides is not possible")

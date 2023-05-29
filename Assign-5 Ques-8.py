# Create an empty list to store the values
values = []

# Loop 10 times to get 10 values
for i in range(10):
  # Get an integer value from the user
  value = int(input("Enter an integer value: "))
  # Append the value to the list
  values.append(value)

# Create empty lists to store positive, negative, odd and even numbers
positive = []
negative = []
odd = []
even = []

# Loop through the values in the list
for value in values:
  # Check if value is positive
  if value > 0:
    # Add it to the positive list
    positive.append(value)
  # Check if value is negative
  elif value < 0:
    # Add it to the negative list
    negative.append(value)
  
  # Check if value is odd
  if value % 2 != 0:
    # Add it to the odd list
    odd.append(value)
  # Check if value is even
  else:
    # Add it to the even list
    even.append(value)

# Print the positive, negative, odd and even numbers
print("The positive numbers are:", positive)
print("The negative numbers are:", negative)
print("The odd numbers are:", odd)
print("The even numbers are:", even)

# Create an empty dictionary to store the counts of each number
counts = {}

# Loop through the values in the list
for value in values:
  # Check if value is already in the dictionary
  if value in counts:
    # Increment its count by one
    counts[value] += 1
  else:
    # Initialize its count to one
    counts[value] = 1

# Print the number of times each number occurs in the list
print("The number of times each number occurs in the list are:")
for key, value in counts.items():
  print(key, ":", value)

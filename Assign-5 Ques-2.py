# Get the range and the number from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
num = int(input("Enter the number to divide by: "))

# Loop through the range
for i in range(start, end + 1):
  # Check if the number is divisible by num
  if i % num == 0:
    # Print the number
    print(i)

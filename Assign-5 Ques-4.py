# Define the number of rows
n = 5

# Loop from 1 to n+1
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

# Loop from n-1 to 0
for i in range(n - 1, 0, -1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

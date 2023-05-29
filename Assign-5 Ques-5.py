
import string

# Get the number of rows from the user
n = int(input("Input the number of rows: "))


alpha = 0

for i in range(1, n + 1):
 
  for j in range(1, i + 1):
    print(string.ascii_uppercase[alpha], end=" ")  
    alpha += 1
    if alpha == 26:
      alpha = 0
 
  print()

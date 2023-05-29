# Define a function to check if a number is prime
def is_prime(number):
  
  if number > 1:
    for i in range(2, number):
      if number % i == 0:
        return False
    return True
 
  else:
    return False

lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

print("The prime numbers in the range", lower, "to", upper, "are:")
for num in range(lower, upper + 1):
  if is_prime(num):
    # Print num
    print(num)

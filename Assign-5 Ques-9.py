# Get the list of words from the user
words = input("Enter a list of words separated by spaces: ").split()

# Create an empty dictionary to store the counts of each word
counts = {}

# Loop through the words in the list
for word in words:
  # Check if word is already in the dictionary
  if word in counts:
    # Increment its count by one
    counts[word] += 1
  else:
    # Initialize its count to one
    counts[word] = 1

# Print the number of occurrences of each word in the list
print("The number of occurrences of each word in the list are:")
for key, value in counts.items():
  print(key, ":", value)

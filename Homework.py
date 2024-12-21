# Define the tuple with the given numbers
numbers = (2, 3, 5, 7, 11)  # You can change these numbers to whatever you like

# Initialize the product variable to 1 (since 1 is the multiplicative identity)
product = 1

# Loop through each number in the tuple and multiply it with the product
for num in numbers:
    product *= num

# Print the result
print("The product of all the numbers in the tuple is:", product)

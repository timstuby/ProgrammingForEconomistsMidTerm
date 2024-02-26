import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Process the list to remove odd numbers and double even numbers
processed_numbers = []
for num in random_numbers:
    if num % 2 == 0:  # Check if even
        processed_numbers.append(num * 2)  # Double even numbers
    else:  # Skip odd numbers
        pass  # No need to add odd numbers to the new list

# Print the final list
print(processed_numbers)


import random

num_list = [random.randint(0, 100) for _ in range(10)]

print("Generated List:", num_list)

# Find the largest number
largest = float('-inf')  # Initialize with the smallest possible value

for num in num_list:
    if num > largest:  # Update largest if a bigger number is found
        largest = num

print(f'The largest number is: {largest}')

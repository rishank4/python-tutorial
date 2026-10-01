def sum_of_positive_numbers(numbers):
     return sum(num for num in numbers if num > 0)

# Example usage
numbers = [3, -1, 7, -4, 2, -6, 10]
result = sum_of_positive_numbers(numbers)
print("Sum of positive numbers:", result)     
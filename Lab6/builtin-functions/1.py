from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

result = multiply_list(numbers)
print("The result of multiplying all the numbers in the list is:", result)
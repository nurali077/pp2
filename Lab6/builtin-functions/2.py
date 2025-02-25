def count_upper_lower(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

input_string = input("Enter a string: ")
upper, lower = count_upper_lower(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}") 
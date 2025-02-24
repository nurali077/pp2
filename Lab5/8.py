import re

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

example_string = "SplitAtUppercase"
result = split_at_uppercase(example_string)
print(result) 
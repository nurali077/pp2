import re

def camel_to_snake(camel_str):

    pattern = r'([a-z])([A-Z])'

    snake_str = re.sub(pattern, r'\1_\2', camel_str).lower()
    return snake_str

camel_case_example = "camelCaseExample"
snake_case_example = camel_to_snake(camel_case_example)
print(snake_case_example) 
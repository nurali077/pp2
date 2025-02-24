import re

def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    replacement = r'\1 \2'
    return re.sub(pattern, replacement, text)
    
text = "InsertSpacesBetweenWords"
result = insert_spaces(text)
print(result) 
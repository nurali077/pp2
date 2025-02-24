import re

def match_string(text):
    pattern = r'a(b*)'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

# Test cases
print(match_string("a"))      # True
print(match_string("ab"))     # True
print(match_string("abb"))    # True
print(match_string("ac"))     # False
print(match_string("b"))      # False
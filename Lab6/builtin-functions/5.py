def all_elements_true(t):
    return all(t)

t = (True, True, True)
print(all_elements_true(t))  # Output: True

t = (True, False, True)
print(all_elements_true(t))  # Output: False
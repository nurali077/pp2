import re

text = "Hello, Brain. How are you?"

result = re.sub(r"[ ,.]", ":", text)
print(result) 
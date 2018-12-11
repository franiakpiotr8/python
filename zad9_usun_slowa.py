# !python
import re

print("==========zadanie6==========")

file = open('example.txt')
try:
    text = file.read()
finally:
    file.close()

words_to_remove = ["się", "i",  "oraz", "nigdy", "dlaczego"]

print(text)

for word in words_to_remove:
    pattern = r'( ' + word + r'\W?)'
    print(pattern)
    text = re.sub(pattern, " ", text, 0, re.IGNORECASE)

print(text)

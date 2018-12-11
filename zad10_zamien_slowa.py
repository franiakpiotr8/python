# !python
import re

print("==========zadanie6==========")

file = open('example.txt')
try:
    text = file.read()
finally:
    file.close()

words_to_swap = {" i":         " temp",
                 " oraz":      " i",
                 " nigdy":     " prawie nigdy",
                 " dlaczego":  " czemu",
                 " temp":      " oraz"}
print(text)

for word in words_to_swap:
    pattern = word + r'\W?)'
    print(pattern)
    text = re.sub(word, words_to_swap.get(word), text, 0, re.IGNORECASE)

print(text)

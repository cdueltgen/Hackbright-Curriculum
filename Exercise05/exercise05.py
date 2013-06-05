from sys import argv

script, filename = argv

f = open(filename)

text = f.read()
text.lower()

letters = [0] * 26
for letter in text:
    index = ord(letter) - ord('a')
    if index >= 0 and index < 26:
        letters[index] += 1


for i in letters:
    print i

f.close()

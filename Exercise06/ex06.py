# open the file, digest it line by line
f = open("test.txt")
words_in_text = {}

#process the file line by line
for line in f:
    # convert all characters in the line to lowercase
    lower_line = line.lower()
    # split the line in to words
    words = lower_line.split(' ')
    # check if the word is already in the dictionary. If not, add it. If so, increment its value
    for word in words:
        # strip out newlines and punctuation
        clean = word.strip(';"!-?.,\n')
        if clean not in words_in_text:
            words_in_text.setdefault(clean, 1)
        else:
            words_in_text[clean] += 1

for word, count in words_in_text.iteritems():
    print word, count

f.close()
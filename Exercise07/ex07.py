f = open("scores.txt")
scores = {}

def alphabetize(my_dict):
    sorted_keys = sorted(my_dict.keys())
    for key in sorted_keys:
        print "Restaurant %s is rated at %s." % (key, my_dict[key])

for line in f:
    split_line = line.split(':')
    split_line[1] = split_line[1].strip('\n')
    scores[split_line[0]] = split_line[1]

alphabetize(scores)

f.close()
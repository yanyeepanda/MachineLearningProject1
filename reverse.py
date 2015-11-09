__author__ = 'Yanyi'

fp = open("Data/vh_sorted_train.txt", "r")
fw = open("Data/re_vh_sorted_train.txt", "w")

childFathers = {}

for line in fp.readlines():
    lineNumbers = line[:-1].split('\t')
    children = lineNumbers[1:]
    if children[0] == "":
        continue
    for c in children:
        if c not in childFathers:
            childFathers[c] = []
        childFathers[c].append(lineNumbers[0])


for k, v in childFathers.iteritems():
    fw.write(k + "\t" + "\t".join(v) + "\n")

fp.close()
fw.close()

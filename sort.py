__author__ = 'Yanyi'

import re
import urllib2
import collections

fp = open("Data/re_vh_sorted_train.txt", "r")
fw = open("Data/rvh_sorted_train.txt.txt", "w")
fatherChildren = dict()

for line in fp.readlines():
    father, sep, children = line.partition("\t")

    if children is None or children == "":
        if father.find("\n"):
            fatherChildren[father[:-2]] = "\n"
    else:
        fatherChildren[father] = children


keylist = []
for k in fatherChildren.keys():
    if k == "":
        continue
    keylist.append(int(k))

keylist.sort()

for key in keylist:
    if key == 6662:
        print fatherChildren["6662"]
    fw.write(str(key) + "\t" + fatherChildren[str(key)])


fp.close()
fw.close()


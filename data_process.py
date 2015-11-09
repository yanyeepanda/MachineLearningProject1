__author__ = 'Yanyi'

import re

fp = open("Data/rvh_sorted_train.txt", "r")

links_dict = {}

for line in fp.readlines():
    dict = {}
    row_text = re.findall(r"[\w']+", line)
    for item in row_text[1:]:
        dict[item] = 1
    links_dict[row_text[0]] = dict
    print(row_text[0] + " " + str(links_dict[row_text[0]]))

import cPickle as pickle
filter_file = open("Data/filterData.p", "wb")
pickle.dump(links_dict, filter_file)
filter_file.close()

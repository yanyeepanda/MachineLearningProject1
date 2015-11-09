__author__ = 'Yanyi'

import re
import cPickle as pickle

# data_dict = {}
re_data_dict = {}

# fo = open("Data/vh_sorted_train.txt", "r")
fr = open("Data/rvh_sorted_train.txt", "r")

# for line in fo.readlines():
#     node = re.findall(r"[\w']+", line)
#     data_dict[node[0]] = node[1:]

for line in fr.readlines():
    node = re.findall(r"[\w']+", line)
    re_data_dict[node[0]] = node[1:]

# o_file = open("Data/dataDict.p", "wb")
# pickle.dump(data_dict, o_file)
# o_file.close()

r_file = open("Data/reDataDict.p", "wb")
pickle.dump(re_data_dict, r_file)
r_file.close()

# fo.close()
fr.close()

__author__ = 'Yanyi'

import re
import cPickle as pickle

test_list = []

with open("Data/test-public.txt", 'r') as file:
     for line in file:
         row = re.findall(r"[\w']+", line)
         edge = (row[1], row[2])
         print(edge)
         test_list.append(edge)

del test_list[0]

data = pickle.load(open("Data/dataDict.p", "rb"))
re_data = pickle.load(open("Data/reDataDict.p", "rb"))

test_feature_dict = {}
test_feature_list = []

num_com_following = 0
num_com_follower = 0

for edge in test_list:
    if edge[0] in data and edge[1] in data and edge[0] in re_data and edge[1] in re_data:
        following1 = data[edge[0]]
        following2 = data[edge[1]]
        num_com_following = len(set(data[edge[0]]).intersection(data[edge[1]]))
        follower1 = re_data[edge[0]]
        follower2 = re_data[edge[1]]
        num_com_follower = len(set(re_data[edge[0]]).intersection(re_data[edge[1]]))
        from_node_following = len(data[edge[0]])
        to_node_follower = len(re_data[edge[1]])
        feature_list = [num_com_following, num_com_follower, from_node_following, to_node_follower]
        test_feature_dict[edge] = feature_list
        test_feature_list.append(feature_list)
        print (str(feature_list))

file_dict = open("Data/testFeatureDict.p", "wb")
pickle.dump(test_feature_dict, file_dict)
file_dict.close()

file_list = open("Data/testFeatureList.p", "wb")
pickle.dump(test_feature_list, file_list)
file_list.close()
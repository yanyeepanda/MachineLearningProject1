__author__ = 'Yanyi'

import re

test_list = []

with open("Data/test-public.txt", 'r') as file:
     for line in file:
         row = re.findall(r"[\w']+", line)
         edge = (row[1], row[2])
         print(edge)
         test_list.append(edge)

del test_list[0]


# import cPickle as pickle
# test_file = open("Data/testdata.p", "wb")
# pickle.dump(edge_list, test_file)
# test_file.close()

import cPickle as pickle
com_follower = pickle.load(open("Data/commonFollower.p", "rb"))
com_following = pickle.load(open("Data/commonFollowing.p", "rb"))

test_feature_list = []

for data in test_list:
    features = []
    if com_follower.has_key(data):

        if com_follower[data] > 0 and com_follower[item] <= 3:
            features.append(1)
        elif com_follower[data] > 3:
            features.append(2)
        else:
            features.append(0)
    else:
        features.append(0)

    if com_following.has_key(data):
        if com_following[data] > 0 and com_following[data] <= 3:
            features.append(1)
        elif com_following[data] > 3:
            features.append(2)
        else:
            features.append(0)
    else:
        features.append(0)

    test_feature_list.append(features)

test_feature_file = open("Data/testFeatures.p", "wb")
pickle.dump(test_feature_list, test_feature_file)
test_feature_file.close()

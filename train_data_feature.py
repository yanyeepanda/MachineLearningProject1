__author__ = 'Yanyi'

__author__ = 'Yanyi'

import re
import cPickle as pickle

edges = pickle.load(open("Data/edge.p", "rb"))

data = pickle.load(open("Data/dataDict.p", "rb"))
re_data = pickle.load(open("Data/reDataDict.p", "rb"))

train_feature_dict = {}
train_feature_list = []

num_com_following = 0
num_com_follower = 0

for edge in edges:
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
        train_feature_dict[edge] = feature_list
        train_feature_list.append(feature_list)
        print (str(feature_list))

file_dict = open("Data/trainFeatureDict.p", "wb")
pickle.dump(train_feature_dict, file_dict)
file_dict.close()

file_list = open("Data/trainFeatureList.p", "wb")
pickle.dump(train_feature_list, file_list)
file_list.close()

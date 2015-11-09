__author__ = 'Yanyi'

import re
import cPickle as pickle
edges = pickle.load(open("Data/edge.p", "rb"))

# com_follower_num_list = []
com_follower_num_dist = {}

matrix = []
with open("Data/train.txt", 'r') as file:
    for line in file:
        row = re.findall(r"[\w']+", line)
        matrix.append(row)

def check_common_follower(edge):
    common_num = 0
    for row in matrix:
        if edge[0] in row[1:] and edge[1] in row[1:]:
            common_num += 1
    return common_num

# for edge in edges:
#     com_follower_num = check_common_follower(edge)
#     print(str(edge)+' '+str(com_follower_num))
#     com_follower_num_list.append((edge, com_follower_num))

for edge in edges:
    com_follower_num = check_common_follower(edge)
    com_follower_num_dist[edge] = com_follower_num
    print(str(edge)+' '+str(com_follower_num))

import cPickle as pickle
com_follower_file = open("Data/commonFollower.p", "wb")
pickle.dump(com_follower_num_dist, com_follower_file)
com_follower_file.close()

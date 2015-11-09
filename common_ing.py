__author__ = 'Yanyi'

import re
import cPickle as pickle
edges = pickle.load(open("Data/edge.p", "rb"))

# com_following_num_list = []
com_following_num_dist = {}

matrix = {}
row1 = []
with open("Data/train.txt", 'r') as file:
    for line in file:
        row = re.findall(r"[\w']+", line)
        row1.append(row[0])
        for item in row1:
            matrix[item] = row[1:]

def check_common_following(edge, row1, matrix):
    common_num = 0
    if edge[0] in row1 and edge[1] in row1:
        common_num = len(set(matrix[edge[0]]).intersection(matrix[edge[1]]))
    return common_num

# for edge in edges:
#     com_following_num = check_common_following(edge, row1, matrix)
#     print(str(edge)+' '+str(com_following_num))
#     com_following_num_list.append((edge, com_following_num))

for edge in edges:
    com_following_num = check_common_following(edge, row1, matrix)
    com_following_num_dist[edge] = com_following_num
    print(str(edge)+' '+str(com_following_num))

import cPickle as pickle
com_following_file = open("Data/commonFollowing.p", "wb")
pickle.dump(com_following_num_dist, com_following_file)
com_following_file.close()
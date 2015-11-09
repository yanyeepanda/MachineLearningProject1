__author__ = 'Yanyi'


import cPickle as pickle
edges = pickle.load(open("Data/edge.p", "rb"))
nodes = pickle.load(open("Data/node.p", "rb"))

num_follower_list = []
for node in nodes:
    num_follower = 0
    for edge in edges:
        if edge[1] == node:
            num_follower = num_follower + 1
    num_follower_list.append((node, num_follower))
    print((node, num_follower))
# print(str(num_follower_list))

import cPickle as pickle
follower_file = open("Data/follower.p", "wb")
pickle.dump(num_follower_list, follower_file)
follower_file.close()

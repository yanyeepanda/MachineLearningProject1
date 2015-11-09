import cPickle as pickle
edges = pickle.load(open("Data/edge.p", "rb"))
nodes = pickle.load(open("Data/node.p", "rb"))
com_follower = pickle.load(open("Data/commonFollower.p", "rb"))
com_following = pickle.load(open("Data/commonFollowing.p", "rb"))

feature_dict = {}
feature_list = []

instances = []
for node1 in nodes:
    for node2 in nodes:
        if node1 is not node2:
            instances.append((node1, node2))


for item in instances:
    features = []
    if com_follower.has_key(item):

        if com_follower[item] > 0 and com_follower[item] <= 3:
            features.append(1)
        elif com_follower[item] > 3:
            features.append(2)
        else:
            features.append(0)
    else:
        features.append(0)

    if com_following.has_key(item):
        if com_following[item] > 0 and com_following[item] <= 3:
            features.append(1)
        elif com_following[item] > 3:
            features.append(2)
        else:
            features.append(0)
    else:
        features.append(0)

    # feature_dict[item] = features
    feature_list.append(features)



link = []
for item in instances:
    if item in edges:
        link.append(1)
    else:
        link.append(0)

import cPickle as pickle
feature_file = open("Data/features.p", "wb")
pickle.dump(feature_list, feature_file)
feature_file.close()

link_file = open("Data/links.p", "wb")
pickle.dump(link, link_file)
link_file.close()

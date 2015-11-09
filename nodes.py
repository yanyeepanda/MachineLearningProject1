import re

# nodes = set()
#
# with open("Data/train.txt", 'r') as file:
#     original_text = file.read()
#     sp_text = re.findall(r"[\w']+", original_text)
#     # sp_text = original_text.split("\t")
#     nodes |= set(sp_text)
# node_list = list(nodes)
# print len(node_list)
#
# import cPickle as pickle
# node_file = open("Data/node.p", "wb")
# pickle.dump(node_list, node_file)
# node_file.close()


node_list = []
fp = open("Data/train.txt", "r")

for line in fp.readlines():
    row = line.split("\t")
    node_list.append(row)

i = 1
total_following = 0
num_following_list = []
for item in node_list:
    num_following = (item[0], (len(item) - 1))
    num_following_list.append(num_following)
    print(str(i)+' '+str(len(item)))
    i = i + 1

import cPickle as pickle
following_file = open("Data/following.p", "wb")
pickle.dump(num_following_list, following_file)
following_file.close()


# for item in node_list:
#     if '\r\n' in item:
#         print 'have'
#         item = node_list.translate(None, '\r\n')
        # node = re.sub('\r\n', '', node)



# node_file = open("Data/node.txt", "w")
# node_file.write(str(list(nodes)))

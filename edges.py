import re

edge_list = []
line_num = 1

with open("Data/train.txt", 'r') as file:
     for line in file:
         edge = ()
         row = re.findall(r"[\w']+", line)
         print (str(line_num) + '  ' + str(len(row)))
         line_num = line_num + 1
         for item in row:
             edge = (row[0], item)
             if edge[0] is not edge[1]:
                 # print edge
                 edge_list.append(edge)

import cPickle as pickle
edge_file = open("Data/edge.p", "wb")
pickle.dump(edge_list, edge_file)
edge_file.close()

# node_file = open("Data/egde.txt", "w")
# node_file.write(str(edge_list))

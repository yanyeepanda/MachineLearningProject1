__author__ = 'Yanyi'

import re

fp = open("Data/vh_sorted_train.txt", "r")
# fw = open("Data/from_node_train.txt", "w")

f_nodes_list = []
for line in fp.readlines():
    row = re.findall(r"[\w']+", line)
    f_nodes_list.append(row[0])
print(f_nodes_list)


# fw.write("\n".join(f_nodes_list))

fp.close()
# fw.close()

fp1 = open("Data/test-public.txt", "r")
# fw1 = open("Data/from_node_test.txt", "w")

f_nodes_list_test = []
for line in fp1.readlines():
    row = re.findall(r"[\w']+", line)
    # f_nodes_list_test.append(row[1])
    f_nodes_list_test.append(row[2])
del f_nodes_list_test[0]
# del f_nodes_list_test[1]
print(f_nodes_list_test)

common_num = len(set(f_nodes_list).intersection(f_nodes_list_test))

print common_num

# fw1.write("\n".join(f_nodes_list_test))

fp1.close()
# fw1.close()
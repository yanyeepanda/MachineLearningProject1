__author__ = 'Yanyi'

# library pgmpy
from pgmpy.models import BayesianModel
# G = BayesianModel()

import pickle
# nodes = pickle.load(open("Data/node.p", "rb"))
edges = pickle.load(open("Data/edge.p", "rb"))
model = BayesianModel(edges)

print(model.active_trail_nodes('378467'))

model_file = open("Data/graphicalModel.p", "wb")
pickle.dump(model, model_file)
model_file.close()



# G.add_nodes_from(nodes)
# G.add_edges_from(edges)
#
# print (gm.active_trail_nodes('378467'))

# from pgmpy.inference import VariableElimination
# from pgmpy.models import BayesianModel
# import numpy as np
# import pandas as pd
# values = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'E'])
# model = BayesianModel([('A', 'B'), ('C', 'B'), ('C', 'D'), ('B', 'E')])
# model.fit(values)
# inference = VariableElimination(model)
# phi_query = inference.query(['A', 'B'])
#
# print(phi_query)

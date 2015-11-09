__author__ = 'Yanyi'

import sys, os

here = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.normpath(os.path.join(here, 'filter')))

from crab.models.classes import MatrixPreferenceDataModel
from crab.models.classes import MatrixBooleanPrefDataModel
from crab.recommenders.svd.classes import MatrixFactorBasedRecommender
# from crab.recommenders.knn.classes import ItemBasedRecommender
# from crab.similarities.basic_similarities import ItemSimilarity
from crab.recommenders.knn.item_strategies import ItemsNeighborhoodStrategy
# from crab.metrics.pairwise import euclidean_distances
import cPickle as pickle

data = pickle.load(open("Data/filterData.p", "r"))

test_data = {'a': {'b': 1, 'c': 1, 'e': 1},
             'b': {'d': 1, 'c': 1, 'e': 1},
             'c': {'a': 1, 'f': 1, 'e': 1}}

modelP = MatrixPreferenceDataModel(data)
modelB = MatrixBooleanPrefDataModel(data)

modelB_file = open("Data/ModelB.p", "wb")
pickle.dump(modelB, modelB_file)
modelB_file.close()

modelP_file = open("Data/ModelP.p", "wb")
pickle.dump(modelP, modelP_file)
modelP_file.close()

items_strategy = ItemsNeighborhoodStrategy()

recsys = MatrixFactorBasedRecommender(model=model, items_selection_strategy=items_strategy, n_features=2)
# print(recsys.recommend('c'))



__author__ = 'Yanyi'

import cPickle as pickle
features = pickle.load(open("Data/features.p", "rb"))
links = pickle.load(open("Data/links.p", "rb"))


import numpy as np
x = np.array(features)
y = np.array(links)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB
clf.fit(x, y)

from sklearn.externals import joblib
joblib.dump(clf, 'Data/NavieBayesModel.pkl')

test_data = pickle.load(open("Data/testFeatures.p", "rb"))

result_list = []
for data in test_data:
    result = clf.predict_proba([data])
    result_list.append()

result_file = open("Data/results.p", "wb")
pickle.dump(result_list, result_file)
result_file.close()


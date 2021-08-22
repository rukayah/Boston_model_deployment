import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor


import pickle

data = load_boston()

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

clf = GradientBoostingRegressor()
clf.fit(x_train, y_train)


predicted = clf.predict(x_test)
expected = y_test


print("RMS: %r " % np.sqrt(np.mean((predicted - expected) ** 2)))
print(data)
#with open("regressor.pkl", "wb") as f:
   # pickle.dump(clf, f)

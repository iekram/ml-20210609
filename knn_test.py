# kNN (k Nearest Neighbors)
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris = datasets.load_iris()
x, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

# print(x_train.shape)
# print(x_train[0])
#
# print(y_train.shape)
# print(y_train)
#
# plt.figure()
# plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap, edgecolor='k', s=20)
# plt.show()


from knn import KNN

clf = KNN(k=7)
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)

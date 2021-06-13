import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

x, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

# fig = plt.figure(figsize=(8, 6))
# plt.scatter(x[:, 0], y, color="b", marker="o", s=30)
# plt.show()


# print(x_train.shape)
# print(y_train.shape)

from linear_regression import LinearRegression

regression = LinearRegression(lr=0.01)
regression.fit(x_train, y_train)
predicted = regression.predict(x_test)


def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted) ** 2)


mse_value = mse(y_test, predicted)
print(mse_value)

y_pred_line = regression.predict(x)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(x_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(x_test, y_test, color=cmap(0.5), s=10)
plt.plot(x, y_pred_line, color='black', linewidth=2, label="Prediction")
plt.show()

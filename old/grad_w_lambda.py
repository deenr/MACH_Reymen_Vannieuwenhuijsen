# used for manipulating directory paths

# Scientific and vector computation for python
import numpy as np

from matplotlib import pyplot


# np.seterr(divide='ignore', invalid='ignore')
from old import utils


def featureNormalize(X):
    # You need to set these values correctly
    X_norm = X.copy()
    mu = np.zeros(X.shape[1])
    sigma = np.zeros(X.shape[1])

    # =========================== YOUR CODE HERE =====================
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X_norm = (X - mu) / sigma

    # ================================================================
    return X_norm, mu, sigma


def computeCostMulti(X, y, theta, lambda_):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # You need to return the following variable correctly
    J = 0

    # ======================= YOUR CODE HERE ===========================
    h = np.dot(X, theta)

    temp = theta
    temp[0] = 0

    J = (1 / (2 * m)) * np.sum(np.square(h - y)) + (lambda_ / (2 * m)) * np.sum(np.square(temp))

    # ==================================================================
    return J


def gradientDescentMulti(X, y, theta, alpha, num_iters, lambda_):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # make a copy of theta, which will be updated by gradient descent
    theta = theta.copy()

    J_history = []

    for i in range(num_iters):
        temp = theta
        temp[0] = 0

        # ======================= YOUR CODE HERE ==========================
        theta = theta - (alpha / m) * ((np.dot(X, theta) - y).dot(X) + lambda_ * temp)
        # =================================================================

        # save the cost J in every iteration
        J_history.append(computeCostMulti(X, y, theta, lambda_))

    return theta, J_history


if __name__ == '__main__':
    # Read comma separated data
    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)
    X, y = data[:, 0:68], data[:, 68]

    m = y.size

    X_norm, mu, sigma = featureNormalize(X)

    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    X_train, Y_train, X_cv, Y_cv, X_test, Y_test = utils.splitDataIntoTrainValTest(X, y, 0.6, 0.3)

    theta = np.zeros(X_train.shape[1])
    alpha = 0.03
    num_iters = 300
    lambda_ = 1

    # J = computeCostMulti(X, y, theta, lambda_)
    theta, J_history = gradientDescentMulti(X, y, theta, alpha, num_iters, 1)
    pyplot.plot(J_history, 'b', label='1')

    pyplot.show()

    print(J_history)

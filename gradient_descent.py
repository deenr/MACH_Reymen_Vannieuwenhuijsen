# used for manipulating directory paths

# Scientific and vector computation for python
import numpy as np

from matplotlib import pyplot

# np.seterr(divide='ignore', invalid='ignore')


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


def computeCostMulti(X, y, theta):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # You need to return the following variable correctly
    J = 0

    # ======================= YOUR CODE HERE ===========================
    h = np.dot(X, theta)

    J = (1 / (2 * m)) * np.sum(np.square(h - y))

    # ==================================================================
    return J


def gradientDescentMulti(X, y, theta, alpha, num_iters):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # make a copy of theta, which will be updated by gradient descent
    theta = theta.copy()

    J_history = []

    for i in range(num_iters):
        # ======================= YOUR CODE HERE ==========================
        theta = theta - (alpha / m) * (np.dot(X, theta) - y).dot(X)
        # =================================================================

        # save the cost J in every iteration
        J_history.append(computeCostMulti(X, y, theta))

    return theta, J_history


if __name__ == '__main__':
    # Read comma separated data
    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)
    X, y = data[:, 0:68], data[:, 68]
    print(X.shape[1])


    m = y.size  # number of training examples

    X_norm, mu, sigma = featureNormalize(X)

    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    # theta = np.random.rand(69)
    theta = np.zeros(X.shape[1])
    J = computeCostMulti(X, y, theta)

    # # Choose some alpha value - change this
    # alpha = 0.001
    # num_iters = 300
    # theta1, J_his1 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    # pyplot.plot(J_his1, 'r', label='alpha = 0.001')
    #
    # # Choose some alpha value - change this
    # alpha = 0.003
    # num_iters = 300
    # theta2, J_his2 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    # pyplot.plot(J_his2, 'g', label='alpha = 0.003')
    #
    # # Choose some alpha value - change this
    # alpha = 0.01
    # num_iters = 300
    # theta3, J_his3 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    # pyplot.plot(J_his3, 'b', label='alpha = 0.01')
    #
    # # Choose some alpha value - change this
    # alpha = 0.03
    # num_iters = 300
    # theta4, J_his4 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    # pyplot.plot(J_his4, 'c', label='alpha = 0.03')
    #
    # # Choose some alpha value - change this
    # alpha = 0.1
    # num_iters = 300
    # theta5, J_his5 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    # pyplot.plot(J_his5, 'm', label='alpha = 0.1')

    # Choose some alpha value - change this
    alpha = 0.3
    num_iters = 300
    theta6, J_his6 = gradientDescentMulti(X, y, theta, alpha, num_iters)
    pyplot.plot(J_his6, 'y', label='alpha = 0.3')

    pyplot.legend()
    pyplot.show()

    print(theta6)

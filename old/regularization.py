# Scientific and vector computation for python
import numpy as np
from matplotlib import pyplot

import utils


# library written for this exercise providing additional functions for assignment submission, and others


def linearRegCostFunction(X, y, theta, lambda_=0.0):
    # Initialize some useful values
    m = y.size  # number of training examples

    # ====================== YOUR CODE HERE ======================

    h = X.dot(theta)
    J = (1 / (2 * m)) * np.sum(np.square(h - y)) + (lambda_ / (2 * m)) * np.sum(np.square(theta[1:]))

    grad = (1 / m) * (h - y).dot(X)

    grad[1:] = grad[1:] + (lambda_ / m) * theta[1:]

    # ============================================================
    return J, grad


def learningCurve(X, y, Xval, yval, lambda_=0):
    # Number of training examples
    m = y.size

    # You need to return these values correctly
    error_train = np.zeros(m)
    error_val = np.zeros(m)

    # ====================== YOUR CODE HERE ======================

    for i in range(1, m + 1):
        theta_t = utils.trainLinearReg(linearRegCostFunction, X[:i], y[:i], lambda_=lambda_)
        error_train[i - 1], _ = linearRegCostFunction(X[:i], y[:i], theta_t, lambda_=0)
        error_val[i - 1], _ = linearRegCostFunction(Xval, yval, theta_t, lambda_=0)

    # =============================================================
    return error_train, error_val


def validationCurve(X, y, Xval, yval):
    # Selected values of lambda (you should not change this)
    lambda_vec = [0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10]

    # You need to return these variables correctly.
    error_train = np.zeros(len(lambda_vec))
    error_val = np.zeros(len(lambda_vec))

    # ====================== YOUR CODE HERE ======================

    for i in range(len(lambda_vec)):
        lambda_try = lambda_vec[i]
        theta_t = utils.trainLinearReg(linearRegCostFunction, X, y, lambda_=lambda_try)
        error_train[i], _ = linearRegCostFunction(X, y, theta_t, lambda_=0)
        error_val[i], _ = linearRegCostFunction(Xval, yval, theta_t, lambda_=0)

    # ============================================================
    return lambda_vec, error_train, error_val


if __name__ == '__main__':
    # data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)
    data = np.loadtxt('real_estate.csv', delimiter=',', dtype=float, skiprows=1)

    X, y = data[:, 0:7], data[:, 7]
    m = y.size

    X_norm, mu, sigma = utils.featureNormalize(X)
    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    # i = 0
    # while i < 68:
    #     plt.subplot(8, 9, i+1)
    #     plt.scatter(X[:, i], y, s=0.5)
    #     i = i + 1
    # plt.show()

    X_train, y_train, X_val, y_val, X_test, y_test = utils.splitDataIntoTrainValTest(X, y, 0.6, 0.3)

    lambda_vec, error_train, error_val = validationCurve(X_train, y_train, X_val, y_val)

    pyplot.plot(lambda_vec, error_train, '-o', lambda_vec, error_val, '-o', lw=2)
    pyplot.legend(['Train', 'Cross Validation'])
    pyplot.xlabel('lambda')
    pyplot.ylabel('Error')
    pyplot.show()

    # plt.scatter(np.linspace(1, X_test.dot(theta).size, X_test.dot(theta).size), X_test.dot(theta), c='r')
    # plt.scatter(np.linspace(1, y_test.size, y_test.size), y_test, c='b')
    # plt.show()

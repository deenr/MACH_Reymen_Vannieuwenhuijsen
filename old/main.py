import numpy as np
from sklearn.linear_model import LinearRegression

import utils


def computeCostMulti(X, y, theta, lambda_=0.):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # You need to return the following variable correctly
    J = 0

    # ======================= YOUR CODE HERE ===========================
    h = np.dot(X, theta)

    temp = theta.copy()
    temp[0] = 0

    J = (1 / (2 * m)) * np.sum(np.square(h - y)) + (lambda_ / (2 * m)) * np.sum(np.square(temp))

    # ==================================================================
    return J


def gradientDescentMulti(X, y, theta, alpha, num_iters, lambda_=0.):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # make a copy of theta, which will be updated by gradient descent
    theta = theta.copy()

    J_history = []

    for i in range(num_iters):
        temp = theta.copy()
        temp[0] = 0

        theta = theta - (alpha / m) * ((np.dot(X, theta) - y).dot(X) + lambda_ * temp)

        # save the cost J in every iteration
        J_history.append(computeCostMulti(X, y, theta))

    return theta, J_history


if __name__ == '__main__':
    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)

    X, y = data[:, 0:68], data[:, 68]
    m = y.size

    X_norm, mu, sigma = utils.featureNormalize(X)
    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    X_train, Y_train, X_cv, Y_cv, X_test, Y_test = utils.splitDataIntoTrainValTest(X, y, 0.6, 0.3)

    # apply your linear regression as you want
    model = LinearRegression()
    model.fit(X_train, Y_train)

    print("Mean squared error: %.2f" % np.mean((model.predict(X_train) - Y_train) ** 2))

    # num_iter = 300
    # alpha = 0.03
    # theta = np.zeros(X.shape[1])
    #
    # J_train_history = []
    # J_cv_history = []
    # lambda_list = [0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10]
    # for lambda_ in lambda_list:
    #     theta_calc, J_history = gradientDescentMulti(X_train, Y_train, theta, alpha, num_iter, lambda_)
    #     pyplot.plot(J_history, 'y', label='J_train')
    #
    #     J_train = computeCostMulti(X_train, Y_train, theta_calc, lambda_)
    #     J_train_history.append(J_train)
    #
    #     J_cv = computeCostMulti(X_cv, Y_cv, theta_calc, lambda_)
    #     J_cv_history.append(J_cv)
    #
    # pyplot.show()
    #
    # pyplot.plot(lambda_list, J_train_history, 'y', label='J_train')
    # pyplot.legend()
    #
    # pyplot.plot(lambda_list, J_cv_history, 'b', label='J_cv')
    # pyplot.legend()
    # pyplot.show()

    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.001, num_iter, 0.1)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='r', label="alpha=0.001")
    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.003, num_iter)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='g', label="alpha=0.003")
    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.01, num_iter)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='b', label="alpha=0.01")
    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.03, num_iter)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='c', label="alpha=0.03")
    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.1, num_iter)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='m', label="alpha=0.1")
    # _, J_history = gradientDescentMulti(X_train, Y_train, theta, 0.3, num_iter)
    # pyplot.plot(np.arange(len(J_history)), J_history, c='k', label="alpha=0.3")
    # pyplot.legend(loc="upper right")
    # pyplot.xlabel('Number of iterations')
    # pyplot.ylabel('Cost J')
    # pyplot.xlim(0, num_iter)
    # pyplot.show()

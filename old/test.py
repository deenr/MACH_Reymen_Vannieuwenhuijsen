import random

import numpy as np
from matplotlib import pyplot

from data_processing import process_data
from grad_w_lambda import gradientDescentMulti, featureNormalize, computeCostMulti


if __name__ == '__main__':
    process_data()
    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)

    X, y = data[:, 0:68], data[:, 68]
    m = y.size

    X_norm, mu, sigma = featureNormalize(X)
    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    X_train, Y_train, X_cv, Y_cv, X_test, Y_test = train_cv_test_split(X, y, 0.6, 0.2)
    # print(Y_train, y)

    alpha = 0.03
    iterations = 300
    theta = np.zeros(X.shape[1])
    # theta = np.random.rand(X.shape[1])
    J_train_history = []
    J_cv_history = []
    # lambda_list = [0, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12, 10]
    lambda_list = np.linspace(0, 10, num=5)
    for lambda_ in lambda_list:
        theta_calc, J_history = gradientDescentMulti(X_train, Y_train, theta, alpha, iterations, lambda_)
        # theta_calc = normalEqn_lambda(X_train, Y_train, lambda_)
        # print(theta_calc)

        J_train = computeCostMulti(X_train, Y_train, theta_calc, lambda_)
        J_train_history.append(J_train)

        J_cv = computeCostMulti(X_cv, Y_cv, theta_calc, lambda_)
        J_cv_history.append(J_cv)

    pyplot.plot(lambda_list, J_train_history, 'y', label='J_train')
    pyplot.legend()

    pyplot.plot(lambda_list, J_cv_history, 'b', label='J_cv')
    pyplot.legend()
    pyplot.show()

    # print(J_train_history, J_cv_history)

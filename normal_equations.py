import numpy as np

import data_processing


def normalEqn(X, y):
    theta = np.zeros(X.shape[1])

    # ===================== YOUR CODE HERE ============================
    theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)

    # =================================================================
    return theta


def normalEqn_lambda(X, y, lambda_):
    # theta = np.zeros(X.shape[1])
    unit_matrix = np.identity(X.shape[1])
    unit_matrix[0][0] = 0
    # ===================== YOUR CODE HERE ============================
    theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + lambda_ * unit_matrix), X.T), y)

    # =================================================================
    return theta


if __name__ == '__main__':
    # Read comma separated data
    # data_processing.prepare_data()

    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)
    X, y = data[:, 0:68], data[:, 68]
    m = y.size
    X = np.concatenate([np.ones((m, 1)), X], axis=1)

    theta = normalEqn_lambda(X, y, 0.33)

    print(theta)

# used for manipulating directory paths
import datetime
import logging

# Scientific and vector computation for python
import numpy as np
import pandas as pd
from matplotlib import pyplot, pyplot as plt


# np.seterr(divide='ignore', invalid='ignore')
from old.data_processing import process_data


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
        logging.info(i)
        # ======================= YOUR CODE HERE ==========================
        theta = theta - (alpha / m) * (np.dot(X, theta) - y).dot(X)
        logging.info(theta)
        # =================================================================

        # save the cost J in every iteration
        cost = computeCostMulti(X, y, theta)
        logging.info(cost)
        J_history.append(cost)



    return theta, J_history


if __name__ == '__main__':
    process_data()
    # Read comma separated data
    data = np.loadtxt('../metro_traffic_data.csv', delimiter=',', dtype=float, skiprows=1)

    df = pd.read_csv(r'../metro_traffic_data.csv')
    X, y = data[:, 0:52], data[:, 52]

    m = y.size  # number of training examples

    X_norm, mu, sigma = featureNormalize(X)

    X = np.concatenate([np.ones((m, 1)), X_norm], axis=1)

    # theta = np.random.rand(69)
    theta = np.zeros(X.shape[1])

    date_now = datetime.datetime.now()
    filename = 'cost_amountOfFeatures_' + str(date_now.strftime("%d-%m-%Y_%H-%M-%S"))
    logging.basicConfig(filename='../log/' + filename + '.log', encoding='utf-8', level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.getLogger('matplotlib.font_manager').disabled = True
    pil_logger = logging.getLogger('PIL')
    pil_logger.setLevel(logging.INFO)

    logging.info('holidays, temp, rain_1h, snow_1h, clouds_all, weather_description feature')
    logging.info('_____________________')
    logging.info(df.head())
    logging.info('_____________________')

    # Choose some alpha value - change this
    alpha = 0.03
    num_iters = 300
    theta, J_history = gradientDescentMulti(X, y, theta, alpha, num_iters)

    f = plt.figure()
    plt.plot(J_history, 'y', label='alpha = 0.3')
    plt.legend()
    plt.xlabel('Amount of iterations')
    plt.ylabel('Cost')
    # plt.show()

    f.savefig('../log/' + filename + '.pdf', bbox_inches='tight')

    print(theta)

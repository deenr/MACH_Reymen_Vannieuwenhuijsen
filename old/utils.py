import random
import sys

import numpy as np
from matplotlib import pyplot
from scipy import optimize

sys.path.append('../..')


# from submission import SubmissionBase


def trainLinearReg(linearRegCostFunction, X, y, lambda_=0.0, maxiter=200):
    """
    Trains linear regression using scipy's optimize.minimize.

    Parameters
    ----------
    X : array_like
        The dataset with shape (m x n+1). The bias term is assumed to be concatenated.

    y : array_like
        Function values at each datapoint. A vector of shape (m,).

    lambda_ : float, optional
        The regularization parameter.

    maxiter : int, optional
        Maximum number of iteration for the optimization algorithm.

    Returns
    -------
    theta : array_like
        The parameters for linear regression. This is a vector of shape (n+1,).
    """
    # Initialize Theta
    initial_theta = np.zeros(X.shape[1])

    # Create "short hand" for the cost function to be minimized
    costFunction = lambda t: linearRegCostFunction(X, y, t, lambda_)

    # Now, costFunction is a function that takes in only one argument
    options = {'maxiter': maxiter}

    # Minimize using scipy
    res = optimize.minimize(costFunction, initial_theta, jac=True, method='TNC', options=options)
    return res.x


def featureNormalize(X):
    """
    Normalizes the features in X returns a normalized version of X where the mean value of each
    feature is 0 and the standard deviation is 1. This is often a good preprocessing step to do when
    working with learning algorithms.

    Parameters
    ----------
    X : array_like
        An dataset which is a (m x n) matrix, where m is the number of examples,
        and n is the number of dimensions for each example.

    Returns
    -------
    X_norm : array_like
        The normalized input dataset.

    mu : array_like
        A vector of size n corresponding to the mean for each dimension across all examples.

    sigma : array_like
        A vector of size n corresponding to the standard deviations for each dimension across
        all examples.
    """
    mu = np.mean(X, axis=0)
    X_norm = X - mu

    sigma = np.std(X_norm, axis=0, ddof=1)
    X_norm /= sigma
    return X_norm, mu, sigma


def plotFit(polyFeatures, min_x, max_x, mu, sigma, theta, p):
    """
    Plots a learned polynomial regression fit over an existing figure.
    Also works with linear regression.
    Plots the learned polynomial fit with power p and feature normalization (mu, sigma).

    Parameters
    ----------
    polyFeatures : func
        A function which generators polynomial features from a single feature.

    min_x : float
        The minimum value for the feature.

    max_x : float
        The maximum value for the feature.

    mu : float
        The mean feature value over the training dataset.

    sigma : float
        The feature standard deviation of the training dataset.

    theta : array_like
        The parameters for the trained polynomial linear regression.

    p : int
        The polynomial order.
    """
    # We plot a range slightly bigger than the min and max values to get
    # an idea of how the fit will vary outside the range of the data points
    x = np.arange(min_x - 15, max_x + 25, 0.05).reshape(-1, 1)

    # Map the X values
    X_poly = polyFeatures(x, p)
    X_poly -= mu
    X_poly /= sigma

    # Add ones
    X_poly = np.concatenate([np.ones((x.shape[0], 1)), X_poly], axis=1)

    # Plot
    pyplot.plot(x, np.dot(X_poly, theta), '--', lw=2)


def splitDataIntoTrainValTest(X, y, train_perc, val_perc):
    # randomly assigning split% rows to training set and rest to test set
    indices = np.array(range(len(X)))

    train_size = round(train_perc * len(X))
    val_size = round(val_perc * len(X))

    random.shuffle(indices)

    train_indices = indices[0:train_size]
    val_indices = indices[train_size + 1:train_size + val_size]
    test_indices = indices[train_size + val_size + 1:len(X)]

    X_train = X[train_indices, :]
    X_val = X[val_indices, :]
    X_test = X[test_indices, :]

    y_column_vector = np.array(y).reshape((len(y), 1))
    y_train = y_column_vector[train_indices, :]
    y_val = y_column_vector[val_indices, :]
    y_test = y_column_vector[test_indices, :]

    return X_train, y_train.T[0], X_val, y_val.T[0], X_test, y_test.T[0]


def calculateR2(y_pred, y_actual):
    # sum of square of residuals
    ssr = np.sum((y_pred - y_actual) ** 2)
    #  total sum of squares
    sst = np.sum((y_actual - np.mean(y_actual)) ** 2)
    # R2 score
    r2_score = 1 - (ssr / sst)
    return r2_score

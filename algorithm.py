# used for manipulating directory paths

# Scientific and vector computation for python
import numpy as np

if __name__ == '__main__':
    # Read comma separated data
    data = np.loadtxt('metro_traffic_data.csv', delimiter=',', dtype='int', skiprows=1)
    X, y = data[:, 0:68], data[:, 68]

    m = y.size  # number of training examples

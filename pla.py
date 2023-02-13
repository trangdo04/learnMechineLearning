import numpy as np

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.mulitvariate_normal(mean[0], cov, N).T
X1 = np.random.mulitvariate_normal(mean[1], cov, N).T

x = np.concatenate((X0, X1), axis = 1)
y = np.concatenate((np.ones))
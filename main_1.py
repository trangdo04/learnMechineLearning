#
# from functools import *
# def square(x):
#     return x * x
#
# def derivative(x):
#     return 2 * x
#
# def different_quotient(f, x, h):
#     return (f(x+h) - f(x)) / h
#
# def partial_difference_quotient(f, v, i, h = 0.00001):
#     w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
#     return (f(w) - f(v)) / h
#
# def estimate_gradient(f, v, h=0.00001):
#     return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]
#
# # def derivative_estimate = partial(difference_quotient, square, h=0.00001)
#
# if __name__ == "__main__":
#     x = int(input())
#     print("derivative(x) :", derivative(x))
#     print("derivative_estimate : ", derivative_estimate(x))
#     a = [-1, -2, 3, 5, 7, 10]
#     b = [1, 4, 9, 25, 49, 100]
    
import random

def sum(x):
    h = 0
    for x_i in x:
        h += x_i
    return h


def target_fn(x, y, theta):
    return y - (x**2) * theta

def gradient_fn(x, y, theta):
    return -2 * x * theta

def in_random_order(data):
    """generator that returns the elements of data in random order"""
    indexes = [i for i, _ in enumerate(data)] # create a list of indexes
    random.shuffle(indexes) # shuffle them
    for i in indexes: # return the data in that order
        yield data[i]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)
    theta = theta_0 # initial guess
    alpha = alpha_0 # initial step size
    min_theta, min_value = None, float("inf") # the minimum so far
    iterations_with_no_improvement = 0
    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 2:
        value = sum( target_fn(x_i, y_i, theta) for x_i, y_i in data )
        if value < min_value:
            # if we've found a new minimum, remember it
            # and go back to the original step size
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
            print("alpha: ", alpha)
        else:
            # otherwise we're not improving, so try shrinking the step size
            # iterations_with_no_improvement += 1
            alpha *= 0.9
            # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta

x = [2, 4, 6, 9]
y = [1, 5, 7, 4]

data = zip(x, y)
print("sum of x : ", sum(x))
print("min_theta la : ", minimize_stochastic(target_fn, gradient_fn, x, y, 3, ))
#print("a la: ", a)



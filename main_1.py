
from functools import *
def square(x):
    return x * x

def derivative(x):
    return 2 * x

def different_quotient(f, x, h):
    return (f(x+h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]

def derivative_estimate = partial(difference_quotient, square, h=0.00001)

if __name__ == "__main__":
    x = int(input())
    print("derivative(x) :", derivative(x))
    print("derivative_estimate : ", derivative_estimate(x))
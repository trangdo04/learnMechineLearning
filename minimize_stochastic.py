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

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def in_random_order(data):
    """generator that returns the elements of data in random order"""
    print("data ", data)
    print("enum: ", enumerate(data))
    indexes = [i for i, _ in enumerate(data)] # create a list of indexes
    random.shuffle(indexes) # shuffle them
    print("hiii")
    print("indexes : ", indexes)
    for i in indexes: # return the data in that order
        print(i)
        yield data[i]
        print("data[i] : ", data[i])


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.02):
    data = zip(x, y)
    theta = theta_0 # initial guess
    alpha = alpha_0 # initial step size
    min_theta, min_value = None, float("inf") # the minimum so far
    iterations_with_no_improvement = 0
    # if we ever go 100 iterations with no improvement, stop
    while iterations_with_no_improvement < 10:
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
            iterations_with_no_improvement += 1
            alpha *= 0.9

        # and take a gradient step for each of the data points
        for x_i, y_i in in_random_order(data):
            print("da vao vong for !")
            # gradient_i = gradient_fn(x_i, y_i, theta)
            # print("gradient_", i, " : ", gradient_i)
            # theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta

if __name__ == '__main__':

    x = [2, 4, 6, 9]
    y = [1, 5, 7, 4]

    data1 = zip(x, y)
    print("random : ", in_random_order(data1))
    print("sum of x : ", sum(x))
    print("min_theta la : ", minimize_stochastic(target_fn, gradient_fn, x, y, 0.45, ))
    #print("a la: ", a)



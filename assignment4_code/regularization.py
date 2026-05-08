#------------------------------------
# Author: T. D. Devlin 
#-----------------------------------

import math
from math import sin, pi
from random import random
import matplotlib.pyplot as plt

def f(x):
    return sin(pi * x)


def generate_training_examples(n=2):
    xs = [random() * 2 - 1 for _ in range(n)]
    return [(x, f(x)) for x in xs]


def fit_without_reg(examples):
    """Computes values of w0 and w1 that minimize the sum-of-squared-errors cost function

    Args:
    - examples: a list of two (x, y) tuples, where x is the feature and y is the label
    """
    w0 = 0
    w1 = 0
    ## BEGIN YOUR CODE ##

    x1, y1 = examples[0]
    x2, y2 = examples[1]

    dx = x2 - x1
    dy = y2 - y1

    w1 = dy / dx
    w0 = y1 - (w1 * x1)

    ## END YOUR CODE ##
    return w0, w1

def fit_with_reg(examples, lambda_hp):
    """Computes values of w0 and w1 that minimize the regularized sum-of-squared-errors cost function

    Args:
    - examples: a list of two (x, y) tuples, where x is the feature and y is the label
    - lambda_hp: a float representing the value of the lambda hyperparameter; a larger value means more regularization
    """
    w0 = 0
    w1 = 0
    ## BEGIN YOUR CODE ##
    #learning rate/step rate/lambda or whatever that 
    #                         greek letter is called i cant remember
    learning_rate = 0.05

    #instructions say to do 1000 iterations
    steps = 1000
    # initialize intercept and slope
    x1, y1 = examples[0]
    x2, y2 = examples[1]
    
    for i in range(steps):
        #placeholder for our y hat
        y_hat = w0 + w1 * x1
        # prediction errors for both points e1 & e2
        e1 = y1 - y_hat
        e2 = y2 - y_hat

        intercept_with_error = -2 * (e1 + e2) + 2 * lambda_hp * w0
        slope_with_error = -2 * (x1 * e1 + x2 * e2) + 2 * lambda_hp * w1
        #update w0(the intercept) and w1(the slope) using gradient descent and L2 regularization
        w0 -= learning_rate * (intercept_with_error)
        w1 -= learning_rate * (slope_with_error)
    ## END YOUR CODE ##
    return (w0, w1)


def test_error(w0, w1):
    n = 100
    xs = [i/n for i in range(-n, n + 1)]
    return sum((w0 + w1 * x - f(x)) ** 2 for x in xs) / len(xs)





if __name__ == "__main__": 
    
    ## BEGIN YOUR SIMULATION CODE ##


    
    

    number_of_trials = 1000
    lambda_hp = 1

    error_without_reg_tot = 0
    error_with_reg_tot = 0
    #perform simulation over 1000 trials 
    for i in range(number_of_trials):
        examples = generate_training_examples(2)
        # 1000 iterations of fit_without_reg with 2 examples for slop and intercept
        w0, w1 = fit_without_reg(examples)

        # 1000 iterations of fit_with_reg with 2 examples for slop and intercept
        w0_reg, w1_reg = fit_with_reg(examples, lambda_hp)
        

        # calculate error for trials in without_reg and add over iterations
        error_without_reg_tot += test_error(w0, w1)

        # calculate error for trials in with_reg and add over iterations
        error_with_reg_tot += test_error(w0_reg, w1_reg)

    print("without regularization avg over 1000 trials:", error_without_reg_tot / number_of_trials)
    print("with regularization avg over 1000 trials:", error_with_reg_tot / number_of_trials)



    ## END YOUR SIMULATION CODE ##



    # IGNORE THIS, JUST TESTING CODE
    # print("------------------------------------------")
    # print("fit_without_reg example:")
    # print("------------------------------------------")

    # # 2 examples this is for testing problem 2 part 3
    # examples = generate_training_examples(2)

    # # print the training data
    # print("examples:", examples)

    # # fit model without regularization
    # w0, w1 = fit_without_reg(examples)

    # # print results
    # print("w0 ( our intercept):", w0)
    # print("w1 (our slope):", w1)

    # # call and print our test error
    # error = test_error(w0, w1)
    # print("test error call returns:", error)
    
    # # we need to check to see if
    # # this code actually is calculating everything properly
    # for x, y in examples:
    #   print("pred:", w0 + w1 * x, "actual:", y)


    # print("END OF fit_without_reg example")
    # print("------------------------------------------")
    # print("fit_with_reg example:")
    # print("------------------------------------------")
    # # test WITH regularization
    # lambda_hp = 1 
    # w0_reg, w1_reg = fit_with_reg(examples, lambda_hp)
    # print("\n--- With Regularization ---")
    # print("w0:", w0_reg)
    # print("w1:", w1_reg)
    # print("Test error:", test_error(w0_reg, w1_reg))


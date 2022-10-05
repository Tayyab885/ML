import numpy as np
#Important Formulas of equations for gradient descent
'''
y_predicted = m_current * x + b_current
#m_current and b_current are the current values of m and b and can be start from 0.
mse(Cost) = (1/n)*sum([val**2 for val in (y-y_predicted)])
m_derivative = -(1/n)*sum(x*(y-y_predicted))
b_derivative = -(1/n)*sum(y-y_predicted)
m_current = m_current - learning_rate*m_derivative # where learning_rate can be 0.001 and can be changeable and increase if the cost is decreasing.
b_current = b_current - learning_rate*b_derivative

'''
'''
SO the result will be the coef and intercept value.
'''


def gradient_descent(x,y):
    m_current = 0
    b_current = 0
    n = len(x)
    iterations = 1000
    #learning_rate = 0.001 # It can be changed and increase if the cost is decreasing.
    # learning_rate = 0.01
    learning_rate = 0.08 # This is best fit for the data.
    for i in range(iterations):
        y_predicted = m_current * x + b_current
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        m_derivative = -(1/n)*sum(x*(y-y_predicted))
        b_derivative = -(1/n)*sum(y-y_predicted)
        
        # Now have to calculate the step size
        m_current = m_current -learning_rate*m_derivative
        b_current = b_current -learning_rate*b_derivative
        
        print(f"m_current: {m_current}, b_current: {b_current},cost: {cost}, iteration: {i}")
    


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
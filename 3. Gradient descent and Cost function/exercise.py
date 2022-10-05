
import numpy as np

def gradient_descent(x,y):
    m_current = 0
    b_current = 0
    n = len(x)
    iteration = 10000
    learning_rate = 0.002
    for i in range(iteration):
        y_predicted = m_current * x * b_current
        
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        m_derrivative = -(1/n)*sum(x*(y-y_predicted))
        b_derrivative = -(1/n)*sum(y-y_predicted)
        
        m_current = m_current - learning_rate*m_derrivative
        b_current = b_current - learning_rate*b_derrivative

        print(f"m_current: {m_current}, b_current: {b_current},cost: {cost}, iteration: {i}")


x = np.array([92,56,88,70,80,49,65,35,66,67])
y = np.array([98,68,81,80,83,52,66,30,68,73])

gradient_descent(x,y)
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:29:12 2021
@author: oh kyu kwon

"""

import numpy as np

#define sigmoid and derivative function
def sigfunc(x,derivative=False):
    if (derivative == True):
        return x*(1-x)
    return 1/(1+np.exp(-x))


# setting values of input, hidden and output unit.

inputs, hiddens, outputs = 3,2,1
learning_rate = 0.2

# training set and labling
X = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
T = np.array([[1],[1],[0],[0],[1],[1],[0],[0]])


W1 = np.array([[0.1,0.2],[0.3,0.4],[0.5,0.5]])
W2 = np.array([[0.5],[0.6]])
B1 = np.array([0.1,0.2])
B2 = np.array([0.3])


def fit():
    global W1,W2,B1,B2
    for i in range(90000):
        for x,y in zip(X,T):
            x = np.reshape(x,(1,-1))
            y = np.reshape(y,(1,-1))

            layer0,layer1,layer2 = predict(x)
            layer2_error = layer2-y
            layer2_delta = layer2_error*sigfunc(layer2,derivative=True)
            
            layer1_error = np.dot(layer2_delta, W2.T)
            layer1_delta = layer1_error*sigfunc(layer1,derivative=True)
            
            W2 += -learning_rate*np.dot(layer1.T, layer2_delta)
            W1 += -learning_rate*np.dot(layer0.T, layer1_delta)
            B2 += -learning_rate*np.sum(layer2_delta, axis = 0)
            B1 += -learning_rate*np.sum(layer1_delta, axis = 0)
            

# 순방향 전파
def predict(x):
    layer0 = x
    Z1 = np.dot(layer0,W1) + B1
    layer1 = sigfunc(Z1)
    Z2 = np.dot(layer1,W2) + B2
    layer2 = sigfunc(Z2)
    
    return layer0, layer1, layer2


def test():
    for x, y in zip(X,T):
        x = np.reshape(x,(1,-1))
        layer0, layer1, layer2 = predict(x)
        print(x, y, layer2) 


fit() 
test()          
from nn import NeuralNetwork
from random import randint
from numpy import random

inputs = [[0, 0], [1, 1], [0, 1], [1,0]]
targets = [[0], [0], [1], [1]]

def output(x):
    if x < 0.5:
        return 0
    else:
        return 1

def test(x):
    
    correct_pred = 0
    for i in range(x):
    
        brain = NeuralNetwork(2, 4, 1)
        for i in range(100000):
            j = randint(0, 3)
            brain.train(inputs[j], targets[j])
        
        t1 = output(brain.feedforward([0,0])[0][0])
        t2 = output(brain.feedforward([1,1])[0][0])
        t3 = output(brain.feedforward([0,1])[0][0])
        t4 = output(brain.feedforward([1,0])[0][0])
    
        print(t1, t2, t3, t4)
        
        if targets[0][0] == t1 and targets[1][0] == t2 and targets[2][0] == t3 and targets[3][0] == t4:
            correct_pred += 1
    
    classification_rate = (correct_pred / x) * 100
    message = "Classification rate: " + str(classification_rate) + "%"
    return message
    
    
# Test 10 times our Neural Network and returns classification rate
test(10)

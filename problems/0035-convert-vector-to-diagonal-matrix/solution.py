import numpy as np

def make_diagonal(x):
	a = []
    for i in range(len(x)):
        temp = []
        for j in range(len(x)):
            if i == j:
                temp.append(x[j])
            else:
                temp.append(0)
        a.append(temp)
    return a
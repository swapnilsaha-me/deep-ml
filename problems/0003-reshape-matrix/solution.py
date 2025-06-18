import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    one_dim = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            one_dim.append(a[i][j])
    reshaped_matrix = []
    if len(one_dim) == new_shape[0] * new_shape[1]:
        idx = 0
        for i in range(new_shape[0]):
            temp = []
            for j in range(new_shape[1]):
                temp.append(one_dim[idx])
                idx = idx + 1
            reshaped_matrix.append(temp)
	return reshaped_matrix
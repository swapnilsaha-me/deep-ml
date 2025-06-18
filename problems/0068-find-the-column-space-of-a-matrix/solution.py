import numpy as np
import copy

def swap_row(mat, r1, r2):
	for i in range(len(mat[r1])):
		temp = mat[r1][i]
		mat[r1][i] = mat[r2][i]
		mat[r2][i] = temp
	return mat

def make_one(mat, row, div):
	for i in range(len(mat[row])):
		mat[row][i] = (mat[row][i] * 1.0) / div
	return mat

def make_up_and_below_zero(mat, row, col):
    for i in range(len(mat)):
        if i == row:
            continue
        mul = -mat[i][col]
        for j in range(len(mat[i])):
            mat[i][j] = (mat[row][j] * mul) + mat[i][j]
    return mat

def reduced_row_echelon_form(mat):
	ans_col = []
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if j < i:
				continue
			if i == j and abs(mat[i][j]) > 1e-9:
				mat = make_one(mat, i, mat[i][j])
				mat = make_up_and_below_zero(mat, i, j)
				ans_col.append(j)
				break
			for k in range(i + 1, len(mat)):
				if mat[k][j] != 0:
					mat = swap_row(mat, i, k)
					break
			if abs(mat[i][j]) > 1e-9:
				mat = make_one(mat, i, mat[i][j])
				mat =
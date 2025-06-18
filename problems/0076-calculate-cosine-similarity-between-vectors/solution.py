
import numpy as np
import math

def cosine_similarity(v1, v2):
	# Implement your code here
	if len(v1) != len(v2):
		return
	a_square = 0.0
	b_square = 0.0
	dot_product = 0.0
	for i in range(len(v1)):
		dot_product = dot_product + (v1[i] * v2[i])
		a_square = a_square + (v1[i] * v1[i])
		b_square = b_square + (v2[i] * v2[i])
	return round(dot_product / (math.sqrt(a_square) * math.sqrt(b_square)), 3)

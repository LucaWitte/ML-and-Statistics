# Implementing distance functions

import math

def manhattan_dist(v1, v2):
    return sum(abs(v1 - v2)) #assuming we obtain np.array and not a list, otherwise convert first

def hamming_dist(v1, v2):
    return sum(abs((v1 > 0) * 1 - (v2 > 0) * 1))

def euclidean_dist(v1, v2):
    return math.sqrt(sum((v1 - v2)**2))

def chebyshev_dist(v1, v2):
    return max(abs(v1-v2))

def minkowski_dist(v1, v2, d): 
    return  sum(abs(v1 - v2)**d)**(1/d)

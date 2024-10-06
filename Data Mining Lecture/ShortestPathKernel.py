import numpy as np

def floyd_warshall(A):
    
    if (np.shape(A)[0] != np.shape(A)[1]):
        print("No adjacency matrix")
        return
    
    S = A # Create new array to maintain information in dataset
 
    for i in range(np.shape(S)[0]):
        for j in range(np.shape(S)[1]):
                if (S[i,j] == 0 and i != j):
                    S[i,j] = int(1e6)
        
    for k in range(np.shape(S)[0]):
        for i in range(np.shape(S)[0]):
            for j in range(np.shape(S)[1]):
                if S[i,j] > S[i,k] + S[k,j]:
                    S[i,j] = S[i,k] + S[k,j]
    return S


def sp_kernel(S1, S2):
    
    sum = 0
    for i1 in range(np.shape(S1)[0]):
        for j1 in range(0,i1):
            for i2 in range(np.shape(S2)[0]):
                for j2 in range(0,i2):
                    if (S1[i1,j1] == S2[i2,j2] and S1[i1,j1] != 0):
                        sum += 1
    return sum

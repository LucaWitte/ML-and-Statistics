# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 19:07:34 2022

@author: Luca Witte
"""
#%%
# Numerical integration
import math 
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

my = 3
sig = 2
a = 0
b = 5

N = 10 # Number of segments

h = (b-a)/N
inputs = np.linspace(a, b, N+1)

def PDF(x, stdev, mean):
    return (1/(math.sqrt(2*math.pi)*stdev)) * np.exp(-0.5 * ((x-mean)/stdev)**2)

PDF_out = PDF(inputs, sig, my)
    
# Composite trapezoidal rule
CTR_a = PDF_out[0]
CTR_b = PDF_out[len(PDF_out)-1]
CTR_sum = np.sum(PDF_out[1:len(PDF_out)-1])

res_CTR = h * (CTR_a/2 + CTR_sum + CTR_b/2)

# Composite Simpson’s rule
CSR_a = PDF_out[0]
CSR_b = PDF_out[len(PDF_out)-1]

CSR_sum_1 = np.sum(PDF_out[1:len(PDF_out)-1])

CSR_sum_2 = np.sum(
    (PDF_out[1:len(PDF_out)]+PDF_out[0:len(PDF_out)-1])/2
    )

res_CSR = h * (CSR_a/6 + CSR_sum_1/3 + CSR_sum_2 * 2/3 + CSR_b/6) 

# True value
#ss.norm(loc=3, scale=2) # where loc is the mean and scale is the std dev
res_true = ss.norm(loc=3, scale=2).cdf(b) - ss.norm(loc=3, scale=2).cdf(a)

N_vec = np.logspace(0.1,4,num=25,base=10,dtype='int')

CTR_list = []
CSR_list = []

for x in N_vec:
    
    N = x
    h = (b-a)/N
    inputs = np.linspace(a, b, N+1)
    
    PDF_out = PDF(inputs, sig, my)
    
    # Composite trapezoidal rule
    CTR_a = PDF_out[0]
    CTR_b = PDF_out[len(PDF_out)-1]
    CTR_sum = np.sum(PDF_out[1:len(PDF_out)-1])

    CTR_list.append(h * (CTR_a/2 + CTR_sum + CTR_b/2))

    # Composite Simpson’s rule
    CSR_a = PDF_out[0]
    CSR_b = PDF_out[len(PDF_out)-1]

    CSR_sum_1 = np.sum(PDF_out[1:len(PDF_out)-1])
    CSR_sum_2 = np.sum((PDF_out[1:len(PDF_out)]+PDF_out[0:len(PDF_out)-1])/2)
    CSR_list.append(h * (CSR_a/6 + CSR_sum_1/3 + CSR_sum_2 * 2/3 + CSR_b/6))
    
    
True_list =  [res_true]*len(N_vec)

plt.plot(N_vec, CSR_list, label = "CSR")
plt.plot(N_vec, CTR_list, label = "CTR")
plt.plot(N_vec, True_list, label = "Correct value")
plt.xscale('log')
plt.show()
    
# relative error

RE_CSR = np.subtract(True_list,CSR_list)
RE_CTR = np.subtract(True_list,CTR_list)

plt.plot(N_vec, RE_CSR, label = "CSR")
plt.plot(N_vec, RE_CTR, label = "CTR")
plt.xscale('log')
plt.yscale('log')
plt.show()

#%%

import math 
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# Lotka-Volterra equations

alpha = 100
beta = 4
gamma = 20
delta = 0.01

count = 0

tol = np.array([[0.01], [0.01]])

# Calculate error
RF_correct = np.array([[gamma/delta], [alpha/beta]])
RF = np.array([[1000], [1000]]) # initial guess

while np.any(abs(RF-RF_correct) > tol):
    
    f_eval = np.array([[alpha * RF[0,0] - beta * RF[0,0] * RF[1,0]],[ -gamma * RF[1,0] + delta * RF[0,0] * RF[1,0]]])
        
        
    a = alpha - beta * RF[1,0]
    b = - beta * RF[0,0]
    c = delta * RF[1,0]
    d = -gamma + delta * RF[0,0]
        
    J_inv = np.multiply( 1/(a*d-b*c), [[d, -b], [-c, a]])
    
    RF = RF - np.matmul(J_inv, f_eval)
    print(RF)
    
    count += 1
    if np.all(abs(RF) == np.array([[0], [0]])):
        print("trivial solution found, try different initial values")
        break
    elif count == 100:
       break





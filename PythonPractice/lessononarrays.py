import numpy as np

print(8-1)
# create and (n x n) with all zeros 
n = 8
z = np.zeros((n, n), dtype=int)
print(z)

# make the middle row and column all ones  
z[n-1,: ] = 1
z[:, n-1] = 1
print(z)

c2 = z+2
print(c2)

c3 = c2**3
print(c3)

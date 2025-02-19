import numpy as np

A = np.array([[2,4],[1,3],[0,0],[0,0]])
print("A =")
print(A)
[U,S,V] = np.linalg.svd(A)
print("U =")
print(U)
print("S =")
print(S)
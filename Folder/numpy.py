# Import of numpy
import numpy as np

#1D array
ay = np.array([2,4,6,8])

ay

#linspace function
np.linspace(0,50,51)


#arange function
np.arange(0,50)

#2D array
ay_2 = np.array([[2,5,6],
                 [3,7,9]])
ay_2

# Null matrix
o = np.zeros([2,6])
o

# Identity matrix
I = np.identity(3)
I

# Random values
ran=np.random.rand(6)
ran

# How to find the shape of an array and transform 1d to 2d array
print(f"Shape is {np.shape(ran)}")

# Random Integer values
rdv = np.random.randint(100,size=(5,5))
rdv

#Normal 1D
""" Simulating values which follows a normal loop"""
np.random.rand(3)

# Normal 2D
np.random.rand(3,3)

# Setting a Seed
print(np.random.rand(3))
print(np.random.rand(3))

np.random.seed(seed=24)
print(np.random.rand(3))

np.random.seed(seed=24)
print(np.random.rand(3))

# Slicing/Indexing/Transformation

mat = np.array([[2,5,6],
                [3,7,9],
                [5,1,3]])
mat

""" choosing submatrix from a matrix"""
mat [0,0]

mat [0:2,0:2]

mat [:,1:3]

# Max of an array
""" By matrix"""
#print(mat,np.max())

arr = np.max(mat)
arr
""" By row """
#print(mat,max(axis = 1))

arr1 = np.amax(mat, axis =1)
arr1

""" By column """
#print(mat,max(axis = 0))

np.amax(mat,axis = 0)

# Min
""" By matrix"""
np.min(mat)

""" By row"""
np.amin(mat,axis=1)

""" By column"""
np.amin(mat,axis=0)

# Mean
np.mean(mat)

np.mean(mat,axis =1)

np.mean(mat,axis =0)

# Standard devaition

np.std(mat)

np.std(mat,axis =1)

np.std(mat,axis =0)

# variance
np.var(mat)

np.var(mat,axis =1)

np.var(mat,axis =0)

# Log function
np.log(mat)

# Exponential function
np.exp(mat)

np.sqrt(mat)

# Concatenating some array
ar1 = mat[:,1]
ar2 = mat[:,2]
print(f"Ar1 is {ar1}")
print(f"Ar2 is {ar2}")
print(np.concatenate((ar1,ar2), axis = 0))

#Concatenate 2 dimensions

ar1 = mat[:,1]
ar2 = mat[:,2]
print(f"Ar1 is {ar1}")
print(f"Ar2 is {ar2}")
print(np.concatenate((ar1,ar2), axis = 0))
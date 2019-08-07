#!/usr/bin/python
import numpy as np
from scipy import linalg

A1 = np.array([[1.0,3.0,3.0,2.0],[2.0,6.0,9.0,5.0], [-1.0,-3.0,3.0,1.0],[1.,2.,-1.,4.]])
b1 = np.reshape(np.array([1.,5.,9,-1.]),(4,1))

A2 = np.reshape(np.array([1.,3.,3.,2.,2.,6.,9.,5.,-1.,-3.,3.,0.,1.,2.,-1.,4.]),(4,4))
b2 = np.reshape(np.array([1.,5.,9,-1.]),(4,1))

A3 = np.reshape(np.array([1.,3.,3.,2.,2.,6.,9.,5.,-1.,-3.,3.,1.]),(3,4))
b3 = np.reshape(np.array([1.,5.,9]),(3,1))

A4 = np.reshape(np.array([1.,3.,3.,2.,2.,6.,9.,5.,-1.,-3.,3.,0,6.,7.,6.]),(5,3))
b4 = np.reshape(np.array([1.,5.,9,1.0,0.0]),(5,1))

print "rank of matix A1 =", np.linalg.matrix_rank(A1)
print "rank of matix A2 =", np.linalg.matrix_rank(A2)
print "rank of matix A3 =", np.linalg.matrix_rank(A3)
print "rank of matix A4 =", np.linalg.matrix_rank(A4)
print "******************\n"

print "The Soultion to A1 x = b1 is"
print linalg.lu_solve(linalg.lu_factor(A1),b1)
print "******************\n"

print "The Soultions to A2 x = b2 is"
print linalg.lstsq(A2,b2)
print "******************\n"

print "The Soultions to A3 x = b3 is"
print linalg.lstsq(A3,b3)
print "******************\n"

print "The Soultions to A4 x = b4 is"
print linalg.lstsq(A4,b4)







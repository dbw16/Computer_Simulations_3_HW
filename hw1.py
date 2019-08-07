#!/usr/bin/python
import numpy as np
from scipy import linalg

def explination(A, b, limit= 1000):
	D = np.zeros_like(A1)
	R = np.zeros_like(A1)
	x = np.zeros_like(b)
	x_new = np.zeros_like(x)

	for i in range(len(D)):
		D[i][i]= A[i][i]
	R = A - D

	B_eval, B_evec = linalg.eig(np.matmul(-np.linalg.inv(D),R))
	A_eval, A_evec = linalg.eig(A)
	print B_eval

def Jac_sol(A, b, limit= 1000):
	print("For the matix")
	print A
	print("and vecter b")
	print b
	D = np.zeros_like(A1)
	R = np.zeros_like(A1)
	x = np.zeros_like(b)
	x_new = np.zeros_like(x)

	for i in range(len(D)):
		D[i][i]= A[i][i]
	R = A - D

	for i in range(limit):
		x_new = np.matmul(np.linalg.inv(D) , b - np.matmul(R ,x) )
		if np.allclose(x, x_new, rtol=1e-10, atol=1e-10):
			break
		x = x_new
		

	print ("Soultion using Jacobi method is:")
	print x
	return x

def LU_decomp_solve(A, b):
	lu, p = linalg.lu_factor(A)
	x = linalg.lu_solve((lu, p), b, True)
	print"Soultion using LU decomp is::"
	print x
	print ("\n")
	return x 


A1 = np.array([[4,1,1,2],[1,6,1,4],[1,1,12,5],[2,4,5,14]])
b = np.reshape(np.array([5,-2,6,9]),(4,1))
A2 = np.array([[2,1,1,2],[1,3,1,4],[1,1,6,5],[2,4,5,7]])

Jac_sol(A1,b)
LU_decomp_solve(A1,b)
Jac_sol(A2,b)
LU_decomp_solve(A2,b)
#explination(A1,b)
#explination(A2,b)









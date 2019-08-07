import numpy as np 
import matplotlib.pyplot as plt

x = [[1,3,3,2],[2,6,9,5],[-1,-3,3,0]]
#x = [[2,-2,1],[5,1,4]]
x_T = np.transpose(x)

eig_vals, eig_vec = np.linalg.eig(np.dot(x,x_T))
empyt , v = np.linalg.eig(np.dot(x_T,x))

eig_vals = np.sort(eig_vals)
eig_vals = np.sqrt(np.abs((eig_vals)))
s = np.zeros((len(eig_vals), len(eig_vals)))
for i in np.arange(len(eig_vals)):
	s[i][i] = eig_vals[len(eig_vals)-1-i]

s_inv = np.linalg.inv(s)

s_inv_extned = np.zeros( (len(empyt),len(empyt)))
for i in range(len(s_inv)):
	s_inv_extned[i][i]=s_inv[i][i]


a = np.dot(x, np.linalg.inv( np.transpose(v) ))
print "my soultion"
print np.dot(a, s_inv_extned)

print"using svd()"
print np.linalg.svd(x)[0]








import numpy as np 
import matplotlib.pyplot as plt



def mean_subtractor(x):
	for i in range(len(x[0])):
		summed = 0
		
		for j in range(len(x)):
			summed = summed + x[j][i]
		
		mean = summed / len(x)
		
		for j in range(len(x)):
			x[j][i] = x[j][i] - mean
	return x



x = np.array([[4.,2.,.6],[4.2,2.1,.59],[3.9,2.0,.58],[4.3, 2.1,.62],[4.1,2.2,.63]])
x = mean_subtractor(x)

print"part 1, new data set x"
print x,"\n"

co_var = np.dot(np.transpose(x),x)/(len(x)-1)
print "part ii the covanrance matrix"
print co_var,"\n"

eig_vals, eigen_vec = np.linalg.eig(co_var)
print "part iii the eigen vector of co_var"
print eigen_vec,"\n"
print"egien eig_vals given by:"
print eig_vals,"\n"

print"part iv  x dot eigen_vec"
print np.dot(x,np.linalg.eig(co_var)[1]),"\n"

print"part v SVD of x"
print np.linalg.svd(x)[0],"\n"

print"part 6"




s_sqrd = np.zeros((3, 3))
for i in np.arange(len(eig_vals)):
	s_sqrd[i][i] = eig_vals[i]

s_inv = np.linalg.inv(s_sqrd)
s_inv_ext = np.zeros((5, 5))
for i in range(3):
	s_inv_ext[i][i]=s_inv[i][i]


eigen_vec = np.linalg.eig(co_var)[1]
plt.plot(np.transpose(np.dot(x,np.linalg.eig(co_var)[1]))[0],np.transpose(np.dot(x,np.linalg.eig(co_var)[1]))[1],".")
plt.show()

'''
from mpl_toolkits.mplot3d import Axes3D
#used to get nice plot of points and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(np.transpose(x)[0],np.transpose(x)[1],np.transpose(x)[2],".")

plt.plot(np.arange(0,1,.01),np.zeros(100),np.zeros(100),"r-")
plt.plot(np.zeros(100),np.arange(0,1,.01),np.zeros(100),"r-")
plt.plot(np.zeros(100),np.zeros(100),np.arange(0,1,.01),"r-")

eigen_vec = np.linalg.eig(co_var)[1]
for i in range(0,3):
		plt.plot([0,eigen_vec[i][0]],[0,eigen_vec[i][1]],[0,eigen_vec[i][2]],"b-")
plt.show()
plt.clear()
'''
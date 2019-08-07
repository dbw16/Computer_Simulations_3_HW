import numpy as np 
import matplotlib.pyplot as plt

def f(A,x, b):
	return .5 * np.dot(np.dot(x, A), x) - np.dot(b, x)

def CG(A, b, plot_error="no"):
	x_i = np.arange(1,len(A) + 1, dtype=np.float)
	r_i = b - np.dot(A, x_i)
	d_i = r_i
	zeros = np.zeros(len(x_i))
	i = 0
	
	if(plot_error == "plot"):
		r_i_list = []
		while(np.allclose(r_i, zeros) == False):
			alpha_i = np.dot(r_i,r_i) / np.dot(np.dot(d_i, A), d_i)
			x_i = x_i + alpha_i * d_i
			r_i_1 = r_i - alpha_i * np.dot(A,d_i)
			beta_i = np.dot(r_i_1,r_i_1) / np.dot(r_i,r_i)
			d_i = r_i_1 +beta_i * d_i
			r_i = r_i_1
			r_i_list.append(np.linalg.norm(r_i))
			i = i +1
		print "this took", i,"iternations"
		return x_i, r_i_list		
	else:
		while(np.allclose(r_i, zeros) == False):
			alpha_i = np.dot(r_i,r_i) / np.dot(np.dot(d_i, A), d_i)
			x_i = x_i + alpha_i * d_i
			r_i_1 = r_i - alpha_i * np.dot(A,d_i)
			beta_i = np.dot(r_i_1,r_i_1) / np.dot(r_i,r_i)
			d_i = r_i_1 +beta_i * d_i
			r_i = r_i_1
			i = i + 1
		print "this took", i,"iternations"
		return x_i	


def sd(A, b, plot_error="no"):
	x_i = np.arange(1,len(A) + 1, dtype=np.float)
	r_i = b - np.dot(A, x_i)
	zeros = np.zeros(len(x_i))
	i = 0
	if (plot_error == "plot"):
		r_i_list=[]
		while(np.allclose(r_i, zeros) == False):
			alpha_i = np.dot(r_i,r_i) / np.dot(np.dot(r_i, A), r_i)
			x_i = x_i + alpha_i * r_i
			r_i_1 = r_i - alpha_i * np.dot(A,r_i)
			beta_i = np.dot(r_i_1,r_i_1) / np.dot(r_i,r_i)
			r_i = r_i_1
			r_i_list.append(np.linalg.norm(r_i))
			i = i +1
		print "this took", i,"iternations"
		return x_i, r_i_list
	else:
		while(np.allclose(r_i, zeros) == False):
			alpha_i = np.dot(r_i,r_i) / np.dot(np.dot(r_i, A), r_i)
			x_i = x_i + alpha_i * r_i
			r_i_1 = r_i - alpha_i * np.dot(A,r_i)
			beta_i = np.dot(r_i_1,r_i_1) / np.dot(r_i,r_i)
			r_i = r_i_1
			i = i +1
		print "this took", i,"iternations"
		return x_i

	


def main():
	A = np.loadtxt("A_matrix.txt", unpack=True)
	b =  np.arange(1,len(A) + 1, dtype=np.float)
	print "our b vector is", b,"\n"
	r_sd = []
	r_cg = []

	print "Using sd method"
	x,r_sd = sd(A, b, "plot")
	print "x = ", x, "\n"
	print "A.x = ", np.dot(A, x),"\n"

	print "Using CG method"
	x, r_cg = CG(A, b, "plot")
	print "x = ", x, "\n"
	print "A.x = ", np.dot(A, x),"\n"

	plt.plot(np.arange(len(r_sd)), r_sd, label="Steapest decent")
	plt.plot(np.arange(len(r_cg)), r_cg, label="Congagent graditant")
	plt.legend(loc="best")
	plt.xlabel("Number of iterations")
	plt.ylabel("Magnatude of residual vector ")
	plt.grid()
	plt.show()

main()
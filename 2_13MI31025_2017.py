import numpy as np
if __name__ == "__main__":
	n = int(raw_input("Enter size of matrix: "))
	a = [[0 for i in range(n)] for j in range(n)]
	x = [1 for j in range(n)]
	e = [0 for j in range(n)]
	for i in range(n):
		for j in range(n):
			a[i][j] = int(raw_input("Value of a[{}][{}]: ".format(i,j)))
	a = np.matrix(a)
	x = np.matrix(x).T
	emax = 0.0
	while (emax>10e-2):
		z = [0 for j in range(n)]
		z += a*x
		zmax = np.matrix.max(np.fabs(z))
		z = z/zmax
		e = z - x
		emax = np.matrix.max(e)
		x = z
	print emax
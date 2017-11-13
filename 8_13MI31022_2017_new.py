from __future__ import division
import numpy as np
import math


def fos(beta, xc, yc, H, n):
	# considering these constants for all slope
	phi = 22 * math.pi / 180
	vr = 1500
	c = 7000

	ym = H
	R = (xc**2 + yc**2)**0.5
	xm = xc + (R**2 - (ym - yc)**2)**0.5

	dx = xm / n

	x_fixed = H / math.tan(beta)

	h_is = []
	alpha_is = []
	w_is = []

	for i in range(n):
		x_left = i * dx
		x_right = (i + 1) * dx
		x_mid = (x_left + x_right) / 2.0
		y_mid = yc - (R**2 - (x_mid - xc)**2)**0.5
		if x_left > x_fixed:
			h_i = H - y_mid
		else:
			y_slope_i = x_mid * math.tan(beta)
			h_i = y_slope_i - y_mid

		alpha_i = math.atan(-(x_mid - xc) / (y_mid - yc))
		w_i = h_i * dx * vr

		h_is.append(h_i)
		alpha_is.append(alpha_i)
		w_is.append(w_i)

	fos_old = 1.0
	fos_new = 0.0
	error = 2.0

	while(math.fabs(error) > 0.0001):
		numerator = 0.0
		denominator = 0.0

		for h_i, alpha_i, w_i in zip(h_is, alpha_is, w_is):
			numerator += ((c + vr * h_i * math.tan(phi)) * dx / math.cos(alpha_i)
						  ) / (1. + (math.tan(alpha_i) * math.tan(phi)) / fos_old)
			denominator += w_i * math.sin(alpha_i)

		fos_new = numerator / denominator
		error = fos_new - fos_old
		fos_old = fos_new

	return fos_new


def fos_matrix(beta, H, n, xl, yl, xr, yr):
	fos_l = []
	import ipdb;ipdb.set_trace()

	for i in range(xl, xr + 1):
		for j in range(yl, yr + 1):
			print i," ",j
			fos_l.append(fos(beta, i, j, H, n))
	fos_l.sort()
	return fos_l


if __name__ == "__main__":
	beta = input("Enter slope angle: ")
	H = input("Enter slope height: ")
	n = input("Enter number of sections: ")
	xl = input("Enter left-most x coordinate: ")
	yl = input("Enter left-most y coordinate: ")
	xr = input("Enter left-most x coordinate: ")
	yr = input("Enter left-most y coordinate: ")

	print fos_matrix(beta,H,n,xl,yl,xr,yr)
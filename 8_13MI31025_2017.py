from __future__ import division
import numpy as np
import math


def fos(beta, xc, yc, H, n):
	# considering these constants for all slope
	phi = 22 * math.pi / 180
	beta = 60 * math.pi / 180
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
		x_left = i*dx
		x_right = (i+1)*dx
		x_mid = (x_left + x_right)/2.0
		y_mid = yc - (R**2 - (x_mid-xc)**2)**0.5
		if x_left > x_fixed:
			h_i = H - y_mid
		else:
			y_slope_i = x_mid*math.tan(beta)
			h_i = y_slope_i - y_mid

		alpha_i = math.atan(-(x_mid-xc)/(y_mid-yc))
		w_i = h_i*dx*vr

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
			numerator += ((c + vr * h_i * math.tan(phi)) * dx / math.cos(alpha_i)) / (1. + (math.tan(alpha_i) * math.tan(phi)) / fos_old)
			denominator += w_i * math.sin(alpha_i)

		fos_new = numerator / denominator
		error = fos_new - fos_old
		fos_old = fos_new

	return fos_new,R


def fos_matrix(beta, H, n, xl, yl, xr, yr):
	min_fos = 100000
	xc = 0
	yc = 0
	r = 0
	for i in range(xl, xr + 1):
		for j in range(yr, yl + 1):
			fos_,R = fos(beta, i, j, H, n)
			if fos_ < min_fos:
				min_fos = fos_
				r = R
				xc = i
				yc = j

	return min_fos,xc,yc,r


if __name__ == "__main__":
	beta = input("Enter slope angle(in degree): ")
	H = input("Enter slope height(in m.): ")
	n = input("Enter number of sections: ")
	xl = input("Enter co-ordinates for Rectangular area of centers of slope failure circles.\n\nEnter top-left-most x coordinate: ")
	yl = input("Enter top-left-most y coordinate: ")
	xr = input("Enter bottom-right-most x coordinate: ")
	yr = input("Enter bottom-right-most y coordinate: ")
	min_fos,xc,yc,r = fos_matrix(beta,H,n,xl,yl,xr,yr)
	print "Using Bishop's method minimum FOS is found out to be: ", min_fos ," by the failure circle of radius " ,r," m. centered at: (",xc,",",yc,")."
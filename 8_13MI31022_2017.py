import numpy as np
import math

beta = 60*math.pi/180
phi = 22*math.pi/180

xc = -5
yc = 60

H = 50
vr = 1500
c = 7000

ym = 50
R = (xc**2+yc**2)**0.5
xm = xc + (R**2 - (H-yc)**2)**(0.5)

n = 10
dx = xm/n
print dx
x_fixed = H/math.tan(beta)

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

	# print x_mid, y_mid

	alpha_i = math.atan(-(x_mid-xc)/(y_mid-yc))
	w_i = h_i*dx*vr

	h_is.append(h_i)
	alpha_is.append(alpha_i)
	w_is.append(w_i)
print h_is
print alpha_is
print w_is
fos_old = 2.0
fos_new = 1.0


while(math.fabs(fos_old - fos_new) > 0.0001):
	
	fos_old = fos_new

	numerator = 0.0
	denominator = 0.0

	for h_i, alpha_i,w_i in zip(h_is, alpha_is,w_is):
		numerator += ((c+vr*h_i*math.tan(phi))*dx/math.cos(alpha_i))/(1.+(math.tan(alpha_i)*math.tan(phi))/fos_old)
		denominator += w_i*math.sin(alpha_i)

	fos_new = numerator/denominator
	
print fos_new
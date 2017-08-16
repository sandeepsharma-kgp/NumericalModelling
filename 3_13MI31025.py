import numpy as np
import scipy.optimize as optimization
l = np.array([25, 50, 75, 100])
Sl = np.array([18, 10, 7, 6])


log_l = np.log(l)
log_Sl = np.log(Sl)


def func(params, xdata, ydata):
    return (ydata - np.dot(xdata, params))
x0 = np.array([0.0, 0.0])
xdata = np.transpose(np.array([[1.0, 1.0, 1.0, 1.0],
                               log_l]))
ydata = log_Sl
log_k, b = optimization.leastsq(func, x0, args=(xdata, ydata))[0]
S = np.exp(log_k + b * np.log(1000)) * 1e6


def fwp(wp, wg, D, F, derivative=False):
    roh = 2600
    h = 3.
    g = 9.8
    a = - 0.36 * S / h
    b = F * (roh * g * D) - S * .64
    c = 2 * wg * F * (roh * g * D)
    d = (roh * g * D) * F * wg**2
    if not derivative:
        return (a * wp**3 + b * wp**2 + c * wp + d)
    else:
        return (3 * a * wp**2 + 2 * b * wp + c)

wp1 = 1000
while True:
    wp2 = wp1 - fwp(wp1, 4.5, 1.35, 200.) / fwp(wp1, 4.5, 200., 1.35, True)
    if abs(wp1 - wp2) < .00001:
        break
    else:
        wp1 = wp2

print S / 1e6
print wp1


table = np.matrix([12., 15., 18., 19.5],
                  [13.5, 16.5, 19.5, 21.],
                  [16.5., 19.5, 22.5, 25.5],
                  [22.5, 25.5, 30., 34.5],
                  [28.5, 34.5, 39., 45.],
                  [39., 42., 45., 48.])


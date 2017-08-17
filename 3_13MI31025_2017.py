import numpy as np
import scipy.optimize as optimization
from matplotlib import cm
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as a3

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
print "Solution of part 1: "
print "Strenth of 1 cubic m. coal block is: ",S / 1e6," MPa"
print "Pillar Width calculated is: " ,wp1," m."


wp_table = np.matrix([[12., 15., 18., 19.5],
                  [13.5, 16.5, 19.5, 21.],
                  [16.5, 19.5, 22.5, 25.5],
                  [22.5, 25.5, 30., 34.5],
                  [28.5, 34.5, 39., 45.],
                  [39., 42., 45., 48.]])

I = pd.Index([60., 75., 120., 195., 300., 360.], name="Depth(in m.)")
C = pd.Index([3., 3.6, 4.2, 4.8], name="Gallery Width(in m.)")

h=3
def fos(wg, wp, D):
    return (( S*(wg*.64+(wp/h)*.36)*wp**2 )/(wp**2+ wg**2)/1e6 )

df_wp = pd.DataFrame(data=wp_table,index=I,columns=C)
df_F = pd.DataFrame(index=I,columns=C)
    
for index, rows in df_wp.iterrows():
    D = index
    for i in range(rows.size):
        wg = rows.index[i]
        wp = df_wp.get_value(D,wg)
        df_F.set_value(D,wg,fos(wg,wp,D))

x = df_F.columns
y = df_F.index
X,Y = np.meshgrid(x,y)
Z = df_F
fig = plt.figure()
ax2 = a3(fig)
surf = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
print "\nSolution df part2: "
print "\nGiven Wp matrix: "
print "\n",df_wp,"\n"
print "\n","Calculated FOS matrix: ","\n"
print df_F
plt.title('Factor of Safety')
plt.xlabel('Gallery Width')
plt.ylabel('Ore Depth')
plt.show()

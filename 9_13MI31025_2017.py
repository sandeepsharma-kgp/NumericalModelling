from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def subsidence_plot(delta, D, W, L, gs=10):
    def influence(r, R):
        return (float)((1 / R**2) * np.exp(-(np.pi * r**2) / (R**2))) * gs**2

    def issafe(i, j, k, l, m, n, gs, R):
        r = (float)(((i - k) * gs)**2 + ((j - l) * gs)**2)**0.5
        if k < m and k >= 0 and l < n and l >= 0 and r <= R:
            return True
        else:
            return False

    R = D * np.tan(np.pi * delta / 180)

    grid = [[0 for r in range(0, (int)((W + 2 * R) / gs))]
            for j in range(0, (int)((L + 2 * R) / gs))]
    sratio = [[0. for r in range(0, (int)((W + 2 * R) / gs))]
              for j in range(0, (int)((L + 2 * R) / gs))]

    grid = np.asarray(grid)
    
    for i in range((int)(R / gs), (int)((L + 1 + R) / gs)):
        for j in range((int)(R / gs), (int)((W + 1 + R) / gs)):
            grid[i][j] = 1

    for i in range(0, grid.shape[0]):
        for j in range(0, grid.shape[1]):
            sratio[i][j] = 0.
            for k in range((int)(i - (R / gs)), (int)(i + 1 + (R / gs))):
                for l in range((int)(j - (R / gs)), (int)(j + 1 + (R / gs))):
                    if issafe(i, j, k, l, grid.shape[0], grid.shape[1], gs, R):
                        sratio[i][j] = sratio[i][
                            j] + (float)(grid[k][l] * influence(((((i - k) * gs)**2) + (((j - l) * gs)**2))**0.5, R))
    Z = sratio
    Z = np.asarray(Z)

    Xi = []
    Yi = []
    Zi = []
    for x in range(0, Z.shape[0]):
        Xi.append(x)
    for y in range(0, Z.shape[1]):
        Yi.append(y)
    for x in range(0, Z.shape[0]):
        zs = []
        for y in range(0, Z.shape[1]):
            zs.append(Z[x][y])
        Zi.append(zs)

    Xi = np.asarray(Xi, dtype='int')
    Yi = np.asarray(Yi, dtype='int')
    x, y = np.meshgrid(Xi, Yi)

    zc = np.array([(float)(Z[xx][yy]) for xx, yy in zip(np.ravel(x), np.ravel(y))])
    zcr = zc.reshape(x.shape)
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax = fig.add_subplot(121, projection='3d')

    ax.plot_surface(x, y, -zcr)

    ax.set_title("Subsidence Profile - 3D")
    ax.set_zlabel("Subsidence Ratio")
    ax.set_xlabel("Along length of the panel")
    ax.set_ylabel("Along width of the panel")

    plt.subplot(122)
    plt.pcolor(x, y, zcr, cmap=cm.coolwarm,
               linewidth=10, antialiased=False)

    plt.title("Subsidence Profile - Top View")
    plt.xlabel("Along length of the panel")
    plt.ylabel("Along width of the panel")
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Subsidence Ratio')
    try:
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
    except:
        pass
    plt.show()

if __name__=="__main__":
	delta = input("Enter delta: ")
	D = input("Enter depth: ")
	L = input("Enter length of the panel: ")
	W = input("Enter width of the panel: ")
	gs = input("Enter grid size(greater than 10 recommended): ")
	print "Please wait for the plot!"
	subsidence_plot(delta,D,W,L,gs)
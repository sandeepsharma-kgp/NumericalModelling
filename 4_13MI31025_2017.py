import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

bd = np.matrix([[44., -1., 40., 42., 40., 39., 37., 36., -1.],
                [42., -1., 43., 42., 39., 39., 41., 40., 36.],
                [37., 37., 37., 35., 38., 37., 37., 33., 34.],
                [35., 38., -1., 35., 37., 36., 36., 35., -1.],
                [36., 35., 36., 35., 34., 33., 32., 29., 28.],
                [38., 37., 35., -1., 30., -1., 29., 30., 32.]])
I = pd.Index([0, 100, 200, 300, 400, 500], name="NS Borehole distance(in m.)")
C = pd.Index([0, 100, 200, 300, 400, 500, 600, 700, 800],
             name="EW Borehole distance(in m.)")
df_bd = pd.DataFrame(data=bd, index=I, columns=C)

ew_variogram = np.array([])
sum_ = 0
for i in range(0, 800, 100):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 100] > 0)]
    if np.square((df[i] - df[i + 100]).values).sum():
        sum_ += np.square((df[i] - df[i + 100]).values).sum() / len(df.index)

ew_variogram = np.append(ew_variogram, sum_)

sum_ = 0
for i in range(0, 700, 100):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 200] > 0)]
    if np.square((df[i] - df[i + 200]).values).sum():
        sum_ += np.square((df[i] - df[i + 200]).values).sum() / len(df.index)

ew_variogram = np.append(ew_variogram, sum_)

sum_ = 0
for i in range(0, 600, 100):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 300] > 0)]
    if np.square((df[i] - df[i + 300]).values).sum():
        sum_ += np.square((df[i] - df[i + 300]).values).sum() / len(df.index)

ew_variogram = np.append(ew_variogram, sum_)

sum_ = 0
for i in range(0, 500, 100):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 400] > 0)]
    if np.square((df[i] - df[i + 400]).values).sum():
        sum_ += np.square((df[i] - df[i + 400]).values).sum() / len(df.index)

ew_variogram = np.append(ew_variogram, sum_)

sum_ = 0
for i in range(0, 400, 100):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 500] > 0)]
    if np.square((df[i] - df[i + 500]).values).sum():
        sum_ += np.square((df[i] - df[i + 500]).values).sum() / len(df.index)

ew_variogram = np.append(ew_variogram, sum_)

ew_variogram = ew_variogram / 2

df_bd_T = df_bd.transpose()
ns_variogram = np.array([])

sum_ = 0
for i in range(0, 500, 100):
    df = df_bd_T.loc[(df_bd_T[i] > 0) & (df_bd_T[i + 100] > 0)]
    if np.square((df[i] - df[i + 100]).values).sum():
        sum_ += np.square((df[i] - df[i + 100]).values).sum() / len(df.index)

ns_variogram = np.append(ns_variogram, sum_)

sum_ = 0
for i in range(0, 400, 100):
    df = df_bd_T.loc[(df_bd_T[i] > 0) & (df_bd_T[i + 200] > 0)]
    if np.square((df[i] - df[i + 200]).values).sum():
        sum_ += np.square((df[i] - df[i + 200]).values).sum() / len(df.index)

ns_variogram = np.append(ns_variogram, sum_)

sum_ = 0
for i in range(0, 300, 100):
    df = df_bd_T.loc[(df_bd_T[i] > 0) & (df_bd_T[i + 300] > 0)]
    if np.square((df[i] - df[i + 300]).values).sum():
        sum_ += np.square((df[i] - df[i + 300]).values).sum() / len(df.index)

ns_variogram = np.append(ns_variogram, sum_)

sum_ = 0
for i in range(0, 200, 100):
    df = df_bd_T.loc[(df_bd_T[i] > 0) & (df_bd_T[i + 400] > 0)]
    if np.square((df[i] - df[i + 400]).values).sum():
        sum_ += np.square((df[i] - df[i + 400]).values).sum() / len(df.index)

ns_variogram = np.append(ns_variogram, sum_)

sum_ = 0
for i in range(0, 100, 100):
    df = df_bd_T.loc[(df_bd_T[i] > 0) & (df_bd_T[i + 500] > 0)]
    if np.square((df[i] - df[i + 500]).values).sum():
        sum_ += np.square((df[i] - df[i + 500]).values).sum() / len(df.index)

ns_variogram = np.append(ns_variogram, sum_)

ns_variogram = ns_variogram / 2


def shear_45_ccw(array):
    ret = []
    for i in range(len(array)):
        ret.append([0] * 14)
        for j in range(len(array[i])):
            ret[i][int(i + j)] = array[i][j]
    return ret

df_bd = pd.DataFrame(data=np.matrix(shear_45_ccw(bd.transpose().tolist())))
df_bd = df_bd.transpose()

ne_variogram = np.array([])
sum_ = 0
for i in range(0, 8):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 1] > 0)]
    if np.square((df[i] - df[i + 1]).values).sum():
        sum_ += np.square((df[i] - df[i + 1]).values).sum() / len(df.index)

ne_variogram = np.append(ne_variogram, sum_)

sum_ = 0
for i in range(0, 7):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 2] > 0)]
    if np.square((df[i] - df[i + 2]).values).sum():
        sum_ += np.square((df[i] - df[i + 2]).values).sum() / len(df.index)

ne_variogram = np.append(ne_variogram, sum_)

sum_ = 0
for i in range(0, 6):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 3] > 0)]
    if np.square((df[i] - df[i + 3]).values).sum():
        sum_ += np.square((df[i] - df[i + 3]).values).sum() / len(df.index)

ne_variogram = np.append(ne_variogram, sum_)

sum_ = 0
for i in range(0, 5):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 4] > 0)]
    if np.square((df[i] - df[i + 4]).values).sum():
        sum_ += np.square((df[i] - df[i + 4]).values).sum() / len(df.index)

ne_variogram = np.append(ne_variogram, sum_)

sum_ = 0
for i in range(0, 4):
    df = df_bd.loc[(df_bd[i] > 0) & (df_bd[i + 5] > 0)]
    if np.square((df[i] - df[i + 5]).values).sum():
        sum_ += np.square((df[i] - df[i + 5]).values).sum() / len(df.index)

ne_variogram = np.append(ne_variogram, sum_)

ne_variogram = ne_variogram / 2

T = np.array([0, 1, 2, 3, 4])
xnew = np.linspace(T.min(), T.max(), 300)

power_smooth = spline(T, ne_variogram, xnew)

plt.plot(xnew, power_smooth)
plt.plot(ne_variogram)
plt.show()

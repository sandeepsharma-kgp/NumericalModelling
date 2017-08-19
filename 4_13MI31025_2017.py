# -*- coding: utf-8 -*-
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

ew_semivariogram = ew_variogram / 2

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

ns_semivariogram = ns_variogram / 2


def rotate45(array):
    rot = []
    for i in range(len(array)):
        rot.append([0] * (len(array)+len(array[0])-1))
        for j in range(len(array[i])):
            rot[i][int(i + j)] = array[i][j]
    return rot

df_bd = pd.DataFrame(data=np.matrix(rotate45(bd.transpose().tolist())))
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

ne_semivariogram = ne_variogram / 2

T = np.array([0, 1, 2, 3, 4])
xnew = np.linspace(T.min(), T.max(), 300)

ew_semivariogram_smooth = spline(T, ew_semivariogram, xnew)
ns_semivariogram_smooth = spline(T, ns_semivariogram, xnew)
ne_semivariogram_smooth = spline(T, ne_semivariogram, xnew)
print "Semivariogram values:"
print "E-W Direction at(100, 200, 300, 400, 500)m.:         ",ew_semivariogram
print "N-S Direction at(100, 200, 300, 400, 500)m.:         ",ns_semivariogram
print "N-E Direction at(100, 200, 300, 400, 500)*(1.414)m.: ",ne_semivariogram

plt.close()
plt.figure(figsize=(30, 6))
plt.subplot(131)
plt.plot(xnew, ew_semivariogram_smooth,'-r',label='smoothed')
plt.plot(T,ew_semivariogram,'-b',label='actual')
plt.legend()
plt.title("E-W Direction")
plt.xlabel('Boreholes distance(1 unit = 100m.)')
plt.ylabel('% Fe')
plt.subplot(132)
plt.plot(xnew, ns_semivariogram_smooth,'-r',label='smoothed')
plt.plot(T,ns_semivariogram,'-b',label='actual')
plt.legend()
plt.title("N-S Direction")
plt.xlabel('Boreholes distance(1 unit = 100m.)')
plt.ylabel('% Fe')
plt.subplot(133)
plt.plot(xnew, ne_semivariogram_smooth,'-r',label='smoothed')
plt.plot(T,ne_semivariogram,'-b',label='actual')
plt.legend() 
plt.title("N-E Direction")
plt.xlabel('Boreholes distance(1 unit = 141.42m.)')
plt.ylabel('% Fe')
plt.show()

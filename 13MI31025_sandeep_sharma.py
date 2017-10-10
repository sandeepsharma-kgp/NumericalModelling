import numpy as np
np.set_printoptions(precision=2)


### to return mulplied matrices
def get_compliance(T_i,c_i):

    C = np.asarray(np.zeros(shape=(4, 4)))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                C[i][j] += T_i[k][i] * c_i[k][j]     #### Transpose of T_i is multiplied with c_i

    K = np.asarray(np.zeros(shape=(4, 4)))
    for i in range(4):
        for j in range(4):
            for k in range(4):
                K[i][j] += C[i][k] * T_i[k][j]      ##### K is multiplied with  T_i
    return np.asmatrix(K)


### to get compliance matrix of a gven joint data
## knn is normal stiffness
## ktt is tangential stiffness
## c_i is compliance matrix in joint axes
## C_i is compliance matrix in universal coordinate axes
## T_i is tranformation matrix 
def compliance(b, d, knn, ktt):
    cnn = (d * knn)**-1
    ctt = (d * ktt)**-1
    c_i = np.matrix([[0., 0., 0., 0.],
                     [0., cnn, 0., 0.],
                     [0., 0., ctt, 0.],
                     [0., 0., 0., 0.]])
    c = np.cos(b * np.pi / 180.)
    s = np.sin(b * np.pi / 180.)
    c2 = c**2
    s2 = s**2
    T_i = np.matrix([[c2, s2, 2 * c * s, 0.],
                     [s2, c2, -2 * c * s, 0.],
                     [c * s, -c * s, s2 - c2, 0.],
                     [0., 0., 0., 1.]])
    C_i = get_compliance(np.asarray(T_i),np.asarray(c_i))

    return C_i


## program starts from here to take information about every joints.
if __name__ == "__main__":
    n = int(raw_input("No. of Joints ,enter n: "))
    C = np.zeros(shape=(4, 4))
    for i in range(n):
        print "\n"
        d = int(raw_input("Enter Joint Spacing(in m.) of Joint-{}: ".format(i + 1)))
        b = int(
            raw_input("Enter Joint orientation angle(in degree) of Joint-{}: ".format(i + 1)))
        knn = int(
            raw_input("Enter normal stiffness(in GPa/m.) of Joint-{}: ".format(i + 1)))
        ktt = int(
            raw_input("Enter tangential stiffness(in GPa/m.) of Joint-{}: ".format(i + 1)))
        C = C + compliance(b, d, knn, ktt)

    print "\nTotal compliance matrix(in 1/GPa) is: \n\n", C

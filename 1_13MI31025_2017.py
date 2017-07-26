from scipy.integrate import quad
from matplotlib import pyplot as plt
import numpy as np

####### poly function to return f(x) for any given x ##################
def poly(x, arr):
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * pow(x, i)
    return ans

########### use simpson 1/3 rule for integration ############
def simpson(a, b, n, arr):
    h = (b - a) / float(n)
    sections = n
    apx = 0.0
    for i in range(1, sections):
        x = a + h * i
        if i % 2 == 0:
            apx += 2 * poly(x, arr)
        else:
            apx += 4 * poly(x, arr)

    apx += poly(a, arr) + poly(b, arr)
    return apx * h / 3.0

########### use trapezoidal 1/3 rule for integration ############
def trapezoidal(a, b, n, arr):
    h = (b - a) / float(n)
    sections = n
    apx = 0.0

    for i in range(1, sections):
        x = a + h * i
        apx += 2 * poly(x, arr)

    apx += poly(a, arr) + poly(b, arr)
    return apx * h / 2.0


######### MAIN START ########################
if __name__ == "__main__":
    ######## Taking input of Polynomial ##################
    degree = int(raw_input("Enter degree of polynomial: "))
    arr = [1] * (degree + 1)
    for i in range(0, degree + 1):
        arr[degree -
            i] = int(raw_input("Enter coefficient of x^{}: ".format(degree - i)))
    a = float(raw_input("Enter lower limit: "))
    b = float(raw_input("Enter upper limit: "))

    ############## Simpson's 1/3rd rule ##########################
    n = int(raw_input("n  is no. of subintervals \nFor Simpson menthod ,enter n(must be even): "))
    print "Area using Simpson 1/3rd rule: ", simpson(a, b, n, arr)

    ######### To analyse simpson's rule getting area at various points ##############
    n_simpson = []
    area_simpson = []
    sections = n
    while(n > sections - 10 and n > 0):
        n_simpson.append(n)
        n -= 2
    n = sections + 2
    while(n <= sections + 100):
        n_simpson.append(n)
        n += 2
    n_simpson.sort()
    for i in n_simpson:
        area_simpson.append(simpson(a, b, i, arr))

    ############## Trapezoidal rule ##########################
    n = int(raw_input("For Trapezoidal menthod ,enter n: "))
    print "Area using Trapezoidal rule: ", trapezoidal(a, b, n, arr)

    ######### To analyse trapezoidal's rule getting area at various points ##############
    n_trapezoidal = []
    area_trapezoidal = []
    sections = n
    while(n > sections - 100 and n - 10 > 0):
        n_trapezoidal.append(n)
        n -= 10
    n = sections + 50
    while(n <= sections + 1000 ):
        n_trapezoidal.append(n)
        n += 50
    n_trapezoidal.sort()
    for i in n_trapezoidal:
        area_trapezoidal.append(trapezoidal(a, b, i, arr))

    ############ Actual Integration Value ############
    I = quad(poly, a, b, args=arr)
    print "Actual area: ", I[0]

    area_trapezoidal = np.array(area_trapezoidal, dtype=float)
    area = np.full((1, len(n_trapezoidal)), I[0], dtype=float)
    area_diff_trapezoidal = area[0] - area_trapezoidal
    area_diff_trapezoidal = np.absolute(area_diff_trapezoidal)
    area_diff_trapezoidal = area_diff_trapezoidal*100/area[0]

    area_simpson = np.array(area_simpson, dtype=float)
    area = np.full((1, len(n_simpson)), I[0], dtype=float)
    area_diff_simpson = area[0] - area_simpson
    area_diff_simpson = np.absolute(area_diff_simpson)
    area_diff_simpson = area_diff_simpson*100/area[0]

    ########### plotting %age error v/s number of subintervals ##########
    plt.close()
    plt.figure(figsize=(30, 6))
    plt.subplot(121)
    plt.plot(n_trapezoidal, area_diff_trapezoidal, 'g--')
    plt.title("TRAPEZOIDAL RULE ANALYSIS")
    plt.xlabel('Number of subintervals')
    plt.ylabel('% Error')
    plt.subplot(122)
    plt.plot(n_simpson, area_diff_simpson, 'r--')
    plt.title("SIMPSON'S 1/3rd RULE ANALYSIS")
    plt.xlabel('Number of subintervals')
    plt.ylabel('% Error')
    plt.ylim(area_diff_trapezoidal[-1] - 10*np.mean(area_diff_trapezoidal), area_diff_trapezoidal[0])
    plt.show()

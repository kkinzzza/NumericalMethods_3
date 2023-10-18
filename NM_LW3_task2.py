import math
from sympy import diff, symbols, sin, cos
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('macosx')

pi = math.pi

x, y = symbols('x y')
a = -1
b = 2
N = 200

def function(x):
    return sin(abs(x)+2.3**x)

# print(diff(function(x), x))

xs1 = [i/100 for i in range(-100, 0, 4)]
xs1.append(-1*10**(-10))
xqq = [1*10**(-10)]
xq1 = [i/100 for i in range(4, 200, 4)]
xs = xs1+xqq+xq1
ys = np.array([function(x) for x in xs])
yss = np.array([(x/abs(x)+2.3**x*math.log(2.3))*(cos(abs(x)+2.3**x)) for x in xs])

# правая РП
xdr1 = [(a+(b-a)*k/N) for k in range(1, N+1)]
ydr1 = [function(x) for x in xdr1]
h = xdr1[N-1]-xdr1[N-2]

deriv1 = [0 for i in range(N)]
for k in range(1, N-1):
    deriv1[k] = (ydr1[k+1]-ydr1[k-1])/(2*h)

# центральная РП
xdr = [(a+(b-a)/(2*N)+(b-a)*k/N) for k in range(0, N)]
ydr = [function(x) for x in xdr]
h = xdr[N-1]-xdr[N-2]

deriv = [0 for i in range(N)]
for k in range(1, N-1):
    deriv[k] = (ydr[k+1]-ydr[k-1])/(2*h)

plt.scatter(xs, yss, color='red', alpha=0.5)
plt.scatter(xdr1, deriv1, color='lime', alpha=0.5)
plt.scatter(xdr, deriv, color='gold', alpha=0.5)
plt.xlabel(r'$x$')
plt.ylabel(r'$f^{\prime}(x)$')
plt.grid(True)
plt.show()
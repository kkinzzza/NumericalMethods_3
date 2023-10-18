import math
import sympy as sp
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy import integrate
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib
matplotlib.use('macosx')

def sin(x):
    return math.sin(x)

pi = math.pi
x = sp.Symbol('x')
a = -1
b = 2
N = 500

def function(x):
    return sin(abs(x)+2.3**x)

print(integrate.quad(function, a, b)[0])

x1 = [(a+(b-a)*k/N) for k in range(0, N+1)]
y1 = [function(x) for x in x1]
xs = [(a+(b-a)/(2*N)+(b-a)*k/N) for k in range(N)]
ys = [function(x) for x in xs]

result = np.array([(b-a)*ys[i]/N for i in range(N)])

delta = integrate.quad(function, a, b)[0] - np.sum(result)

print(np.sum(result))
print(delta)

fig, ax = plt.subplots()
ax.plot(x1, y1, color='lime')
for i in range(N):
    ax.add_patch(Rectangle((x1[i],0), (b-a)/N, ys[i]))

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
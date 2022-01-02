import matplotlib
matplotlib.use("TkAgg")
from matplotlib.pyplot import *
import numpy as np
from math import *
def f1(t):
    return sin(t)*cos(t)*log(fabs(t))
x=np.vectorize(f1)
def f2(t):
    return sqrt(fabs(t))*cos(t)
y=np.vectorize(f2)
t=np.arange(-1,1,1/1000)
plot(x(t),y(t))
show()
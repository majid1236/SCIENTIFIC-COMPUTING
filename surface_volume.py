import numpy as np
from scipy import integrate

def integrand(y, x):
    return x**2 + y**2

volume, error = integrate.dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)

print(f"Volume under z = x² + y² over [0,1]x[0,1]: {volume:.4f}")

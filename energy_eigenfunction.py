from numpy.polynomial.hermite import *
import numpy as np
import math
from matplotlib import pyplot as plt


hbar = 1
pi = np.pi

def HO_Func(K, m,  n, r):
    
  w = np.sqrt(K/m)
  psi = []
  herm_coeff = []

  for i in range(n):
      herm_coeff.append(0)
  herm_coeff.append(1)

  for x in r:
    psi.append(math.exp(-m*w*x**2/(2*hbar)) * hermval((m*w/hbar)**0.5 * x, herm_coeff))
  # normalization factor for the wavefunction:
  psi = np.multiply(psi, 1 / (math.pow(2, n) * math.factorial(n))**0.5 * (m*w/(pi*hbar))**0.25)

      
  return psi

x = np.linspace(-5,5,200)
psi = HO_Func(1, 1, 2, x)

plt.plot(x, psi)

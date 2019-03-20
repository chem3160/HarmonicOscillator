from numpy.polynomial.hermite import *
import numpy as np
import math
from matplotlib import pyplot as plt


h_bar = 1
pi = np.pi
def HO_Func(state, xgrid, k, mu):
    
  w = np.sqrt(k/mu)
  psi = []
  herm_coeff = []

  for i in range(state):
      herm_coeff.append(0)
  herm_coeff.append(1)

  for x in xgrid:
    psi.append(math.exp(-mu*w*x**2/(2*h_bar)) * hermval((mu*w/h_bar)**0.5 * x, herm_coeff))
  # normalization factor for the wavefunction:
  psi = np.multiply(psi, 1 / (math.pow(2, state) * math.factorial(state))**0.5 * (mu*w/(pi*h_bar))**0.25)

      
  return psi

x = np.linspace(-5,5,200)
psi = HO_Func(3, x, 1, 1)

plt.plot(x, psi)
plt.show()

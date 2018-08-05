#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:43:02 2018

@author: matias

################################################################################################

Programa que muestra el fenomeno de la perdidad de significancia con el comportamiento al calcular
la funcion sqrt(x**2+1)-1 cuando x tiende a cero, con dos diferentes formatos de numeros, donde,
por las aproximaciones automaticas de cada formato.

""" 

import numpy as np
from decimal import *
import matplotlib.pylab as plt

print ''

x = [1.89e-9, 1.99e-9, 2.09e-9]
N = len(x)

# Valores esperados
expect = [0.0000000000000000017860499999999, 0.0000000000000000019800499999999, 0.0000000000000000021840499999999]

# Calculo de la funcion con formato por defecto (float = float64)
fx = []
for i in range(N):
    fx.append(np.sqrt(x[i]**2+1.0)-1.0)

# Calculo de la funcion con formato "decimal"
fx_dec = []
for i in range(N):
    x_dec = Decimal(x[i])
    fx_dec.append(np.float(np.sqrt(x_dec**2+Decimal(1.0))-Decimal(1.0)))


# Printing en la consola para mayor claridad
print 'Valores esperados:', expect
print ''
print 'Valores con formato "float" y libreria "numpy":', fx
print ''
print 'Valores con libreria "decimal":', fx_dec


# Ploteo
plt.figure(1)
plt.subplot(211)

plt.plot(x, expect, '^', label="Valores exactos")
plt.plot(x, fx, label="x.dtype=float")
plt.plot(x, fx_dec, label="x.dtype=Decimal")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=1.)

plt.savefig("loss-of-significance.png")
plt.show()
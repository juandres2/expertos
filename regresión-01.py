#!/usr/bin/env python
# coding: utf-8

# <img style="float:left; width:600px;" src="slider/slider-001.PNG">

# <img style="float:left; width:600px;" src="slider/slider-002.PNG">

# In[1]:


# PREPARACIÓN DE DATOS PARA REGRESIÓN

# "np" y "plt" son "alias" para NumPy y Matplotlib, respecivamente.
# --------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# X representa el diámetro de las pizzas.
# Una convención de scikit-Learn es nombrar la matriz 
# del vector independiente con el mombre X.
# Las letras mayúsculas indican matrices, y las letras minúsculas indican vectores.
# El valor -1 fuerza a numpy a calcular el valor que mejor se acomoda a la matriz
# Para el caso mostrado, genera una matriz de 5 filas y 1 columna
# --------------------------------------------------------------------------------
X = np.array([6, 8, 10, 14, 18]).reshape(-1, 1)

print("Matriz X: \n", X)

# y es un vector que representa los precios de las pizzas
# --------------------------------------------------------------------------------
y = [7, 9, 13, 17.5, 18]

# Se genera la figura
# --------------------------------------------------------------------------------
plt.figure()
plt.title('Precio de la Pizza contra el diámetro')
plt.xlabel('Diametro en pulgadas')
plt.ylabel('Precio en dólares')

# Se genera la grafica X contra y, color azul (blue), tamaño del punto, 20
# --------------------------------------------------------------------------------
plt.plot(X, y, 'b.', markersize=20)

# Se definen los ejes, horizontal y vertical
# --------------------------------------------------------------------------------
plt.axis([0, 25, 0, 25])

# Se genera una retícula
# --------------------------------------------------------------------------------
plt.grid(True)

# Se grafica la función sobre la interfaz visual
# --------------------------------------------------------------------------------
plt.show()


# In[ ]:





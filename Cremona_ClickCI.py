# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:11:46 2020

@author: GastonRA
"""
import numpy as np
import matplotlib
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt




#Parametros -----------------------------
t0 = 0
tf = 2000

a = 1.32843

#Memoria ---------------------------------

#Iteraciones finales
x1 = [0.5]*(tf-t0)
x2 = [0]*(tf-t0)

print(np.cos(a), np.sin(a))

def cremona(a,xn,yn):
  xk = xn * np.cos(a) - (yn - xn*xn) * np.sin(a)
  yk = xn * np.sin(a) + (yn - xn*xn) * np.cos(a)

  return xk, yk


def Cremona_Cicle(xi,yi,a_,tf = 2000,):
  x1 = [xi]*(tf)
  x2 = [yi]*(tf)
  for i in range(tf-1):
    x0 = x1[i]
    y0 = x2[i]
    x1[i+1] = x0 * np.cos(a_) - (y0 - x0*x0) * np.sin(a_)
    x2[i+1] = x0 * np.sin(a_) + (y0 - x0*x0) * np.cos(a_)
  a.add_artist(plt.scatter(x1,x2, s = 0.1, marker='.'))
  canvas.draw()






def onclick(event):
    ix, iy = float(event.xdata), float(event.ydata)
    
    Cremona_Cicle(ix, iy, 1.32843)
    print(ix, iy)



root = tk.Tk()
circle1 = plt.Circle((0, 0), 1, color='white')

f = plt.figure()
a = f.add_subplot(111)
f, a = plt.subplots()
a.add_artist(circle1)
a.set_xlim(-1.1, +1.1)
a.set_ylim(-1.1, +1.1)

#a.plot(circle1)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas.mpl_connect('button_press_event', onclick)

canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()



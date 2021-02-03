# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:47:35 2020

@author: GastonRA
"""

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
a = 3.43
b = 0.31


t0 = 100


print(np.cos(a), np.sin(a))

def disprey(a,b,xn,yn):
  xk = a * xn*(1-xn)-xn*yn
  yk = (1/b) * xn*yn

  return xk, yk


def Disprey_Cicle(xi,yi,a_,b_,tf):
  x1 = [xi]*(tf)
  x2 = [yi]*(tf)
  for i in range(tf-1):
    x0 = x1[i]
    y0 = x2[i]
    x1[i+1], x2[i+1] = disprey(a_,b_,x0,y0)
  a.add_artist(plt.scatter(x1,x2, s = 0.1, marker='.'))
  canvas.draw()






def onclick(event):
    ix, iy = float(event.xdata), float(event.ydata)
    
    Disprey_Cicle(ix,iy,2.7,0.31,1000)
    print(ix, iy)



root = tk.Tk()
circle1 = plt.Circle((0, 0), 1, color='white')

f = plt.figure()
a = f.add_subplot(111)
f, a = plt.subplots()
a.add_artist(circle1)
a.set_xlim(0.1,0.5)
a.set_ylim(0,1.6)

#a.plot(circle1)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas.mpl_connect('button_press_event', onclick)

canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()



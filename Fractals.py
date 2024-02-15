import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot():
    def __init__(self, name, xmin, xmax, ymin, ymax, width, height, max_iter):
        self.name = name
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.max_iter = max_iter
        self.mset = self.mandelbrot_set()

    def mandelbrot(self, c):
        z = 0 
        for n in range(self.max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return self.max_iter
        
    def mandelbrot_set(self):
        x = np.linspace(self.xmin, self.xmax, self.width)
        y = np.linspace(self.ymin, self.ymax, self.height)
        mset = np.zeros((self.height, self.width))

        for i in range(self.width):
            for j in range(self.height):
                c = complex(x[i], y[j])
                mset[j,i] = self.mandelbrot(c)
        return mset
    
    def display_fractal(self):
        plt.imshow(self.mset, extent=(self.xmin, self.xmax, self.ymin, self.ymax))
        plt.title(self.name)
        plt.set_cmap()
        plt.show()

mandalbrot = Mandelbrot("MandelbrotSet", xmin=-2, xmax=1, ymin=-1, ymax=1, width=1000, height=1000, max_iter=256)
mandalbrot.display_fractal()



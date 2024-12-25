import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


class Mandelbrot():
    def __init__(self, xmin, xmax, ymin, ymax, width, height, max_iter):
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
        plt.set_cmap("hot")
        plt.show()


class Julia():
    def __init__(self, h_range, w_range, max_iter):
        self.h_range = h_range
        self.w_range = w_range
        self.max_iter = max_iter
        self.jset = self.julia_set()
        
    def julia_set(self):
        y, x = np.ogrid[-1.5:1.5:self.h_range*1j, -1.5:1.5:self.w_range*1j]
        z = x + y*1j
        a = -0.8 + 0.156j
        iter_div = np.zeros(z.shape)

        for h in range(self.h_range):
            for w in range(self.w_range):
                c = z[h, w]
                for i in range(self.max_iter):
                    z[h, w] = z[h, w]**2 + a
                    if z[h, w] * np.conj(z[h, w]) > 4:
                        iter_div[h, w] = i
                        break
        return iter_div

    def draw_julia(self):
        plt.imshow(self.jset, extent=(-1.5, 1.5, -1.5, 1.5), cmap="magma", norm=LogNorm())
        plt.axis("off")
        plt.show()



class BurningShip():
    def __init__(self, x, y, num_iterations, xmin=-2, xmax=2, ymin=-2, ymax=2, width=1000, height=1000):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.width = width
        self.height = height
        self.num_iterations = num_iterations
        self.mset = self.generate_burning_ship(x, y)

    def mandelbrot(self, x, y, num_iterations):
        c = complex(x, y)
        zx = 0
        zy = 0
        
        for i in range(num_iterations):
            next_zx = zx**2 - zy**2 + x
            zy = abs(2 * zx * zy) + y
            zx = next_zx
            z = complex(zx, zy)**2 + c
            if abs(z) > 4:
                return i
        return num_iterations - 1

    def generate_burning_ship(self, x, y):
        mset = np.zeros((self.height, self.width))

        for i in range(self.height):
            for j in range(self.width):
                zx = self.xmin + j * (self.xmax - self.xmin) / self.width
                zy = self.ymin + i * (self.ymax - self.ymin) / self.height
                mset[i, j] = self.mandelbrot(zx, zy, self.num_iterations)

        return mset

    def display_burning(self):
        plt.imshow(self.mset, extent=(self.xmin, self.xmax, self.ymin, self.ymax), cmap="twilight_shifted", norm=LogNorm(), aspect='auto')
        plt.axis('off')  # Turn off axis
        plt.grid(False)  # Turn off grid
        plt.tight_layout()
        plt.show()
        

class Tricorn():
    def __init__(self, width, height, max_iter):
        self.width = width
        self.height = height
        self.max_iter = max_iter

    def tricorn(self, x, y):
        zx = x
        zy = y
        iteration = 0

        while zx*zx + zy*zy < 4 and iteration < self.max_iter:
            xtemp = zx*zx - zy*zy + x
            zy = -2*zx*zy + y
            zx = xtemp
            iteration += 1

        if iteration == self.max_iter:
            return 0  # Inside color
        return iteration / self.max_iter  # Color based on iteration count

    def tricorn_set(self):
        tset = np.zeros((self.height, self.width))

        # Scaling factors for Mandelbrot X and Y scale
        x_scale = np.linspace(-2.5, 1, self.width)
        y_scale = np.linspace(-1, 1, self.height)

        for i, x in enumerate(x_scale):
            for j, y in enumerate(y_scale):
                tset[j, i] = self.tricorn(x, y)
        return tset

    def display_fractal(self):
        plt.imshow(self.tricorn_set(), cmap='magma', extent=(-2.5, 1, -1, 1), aspect='auto')
        plt.axis('off')  # Turn off axis
        plt.grid(False)  # Turn off grid
        plt.tight_layout()
        plt.show()
        
        



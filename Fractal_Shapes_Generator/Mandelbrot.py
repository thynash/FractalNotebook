import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def generate_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter=256):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            c = complex(r1[i], r2[j])
            mandelbrot_image[j, i] = mandelbrot(c, max_iter)
    return mandelbrot_image

mandelbrot_description = """
### Mandelbrot Set

The Mandelbrot set is a famous fractal in mathematics, defined by the set of complex numbers c for which the sequence z_(n+1) = z_n^2 + c (starting with z_0 = 0) does not tend toward infinity, no matter how many times the process is repeated.

Its boundary forms one of the most intricate and beautiful patterns in mathematics, demonstrating infinite complexity and self-similarity at every scale. By adjusting the number of iterations, you can explore more or less detail in its structure.

Use the slider below to control the maximum iterations in the visualization and discover fascinating shapes in the Mandelbrot set!
"""


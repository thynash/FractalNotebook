import numpy as np
import matplotlib.pyplot as plt
import os

# Create an output directory for the images
output_dir = '../Fractal_Shapes'
# --- Mandelbrot Set ---
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

# Generate and save the Mandelbrot set image
mandelbrot_img = generate_mandelbrot_set(-2.0, 1.0, -1.5, 1.5, 800, 600)
plt.imshow(mandelbrot_img, cmap='hot', extent=(-2, 1, -1.5, 1.5))
plt.colorbar()
plt.title('Mandelbrot Set')
plt.savefig(os.path.join(output_dir, 'Mandelbrot.png'))
plt.close()


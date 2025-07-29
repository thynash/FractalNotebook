import numpy as np
import matplotlib.pyplot as plt
import os
output_dir="../Fractal_Shapes"
def julia(c, max_iter):
    def func(z):
        for i in range(max_iter):
            z = z*z + c
            if abs(z) > 2:
                return i
        return max_iter
    return func

def generate_julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter=256):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    julia_image = np.zeros((height, width))
    func = julia(c, max_iter)
    for i in range(width):
        for j in range(height):
            z = complex(r1[i], r2[j])
            julia_image[j, i] = func(z)
    return julia_image

# Generate and save the Julia set image
c = complex(-0.8, 0.156)
julia_img = generate_julia_set(c, -2.0, 2.0, -2.0, 2.0, 800, 800)
plt.imshow(julia_img, cmap='cool', extent=(-2, 2, -2, 2))
plt.colorbar()
plt.title('Julia Set')
plt.savefig(os.path.join(output_dir, 'Julia.png'))
plt.close()


import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Newton_fractal"

def newton_fractal(f, df, bounds, res=400, max_iter=20):
    xmin, xmax, ymin, ymax = bounds
    x = np.linspace(xmin, xmax, res)
    y = np.linspace(ymin, ymax, res)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    for i in range(max_iter):
        Z -= f(Z)/df(Z)
    img = np.angle(f(Z))
    return img

def f(z): return z**3 - 1
def df(z): return 3*z**2

def generate_newton_fractal(order):
    img = newton_fractal(f, df, (-1.5,1.5,-1.5,1.5), res=600, max_iter=5+order*2)
    plt.figure(figsize=(8,8))
    plt.imshow(img, extent=(-1.5,1.5,-1.5,1.5), cmap='hsv')
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'newton_fractal_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 11), desc="Newton Fractal"):
        generate_newton_fractal(order)


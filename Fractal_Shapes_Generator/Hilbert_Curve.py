import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Hilbert_curve"

def hilbert(ax, x, y, xi, xj, yi, yj, n):
    if n <= 0:
        ax.plot(x + (xi+yi)/2, y + (xj+yj)/2, 'ro')
    else:
        hilbert(ax, x, y, yi/2, yj/2, xi/2, xj/2, n-1)
        hilbert(ax, x+xi/2, y+xj/2, xi/2, xj/2, yi/2, yj/2, n-1)
        hilbert(ax, x+xi/2+yi/2, y+xj/2+yj/2, xi/2, xj/2, yi/2, yj/2, n-1)
        hilbert(ax, x+xi/2+yi, y+xj/2+yj, -yi/2, -yj/2, -xi/2, -xj/2, n-1)

def generate_hilbert_curve(order):
    plt.figure(figsize=(7,7))
    ax = plt.gca()
    hilbert(ax, 0, 0, 1, 0, 0, 1, order)
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'hilbert_curve_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 8), desc="Hilbert Curve"):
        generate_hilbert_curve(order)


import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Peano_curve"

def peano(ax, x, y, size, n):
    if n == 0:
        ax.plot([x], [y], 'bo', markersize=1)
    else:
        newSize = size / 3
        offsets = [(0,0), (0,newSize), (0,2*newSize),
                   (newSize,2*newSize), (newSize,newSize), (newSize,0),
                   (2*newSize,0), (2*newSize,newSize), (2*newSize,2*newSize)]
        for dx, dy in offsets:
            peano(ax, x+dx, y+dy, newSize, n-1)

def generate_peano_curve(order):
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    peano(ax, 0, 0, 1, order)
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'peano_curve_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 6), desc="Peano Curve"):  # Higher orders are very slow
        generate_peano_curve(order)


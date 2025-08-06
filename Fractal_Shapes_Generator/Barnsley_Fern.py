import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Barnsley_fern"

def barnsley_fern(n=10000):
    x = y = 0
    xs, ys = [], []
    for _ in range(n):
        r = np.random.random()
        if r < 0.01:
            x, y = 0, 0.16*y
        elif r < 0.86:
            x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif r < 0.93:
            x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
        xs.append(x)
        ys.append(y)
    return xs, ys

if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    for mag in tqdm(range(1, 11), desc="Barnsley Fern"):
        n_points = mag * 10000
        x, y = barnsley_fern(n=n_points)
        plt.figure(figsize=(7,10))
        plt.scatter(x, y, s=0.1, color='green')
        plt.axis('off')
        plt.title(f'Barnsley Fern ({n_points} points)')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'barnsley_fern_points_{n_points}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
        plt.close()


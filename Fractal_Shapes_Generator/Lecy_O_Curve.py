import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Levy_C_curve"

def levy_curve(ax, p1, p2, n):
    if n == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b')
    else:
        mid = (
            (p1[0] + p2[0])/2 + (p1[1] - p2[1])/2,
            (p1[1] + p2[1])/2 + (p2[0] - p1[0])/2
        )
        levy_curve(ax, p1, mid, n-1)
        levy_curve(ax, mid, p2, n-1)

def generate_levy_curve(order):
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    levy_curve(ax, (0,0), (1,0), order)
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'levy_c_curve_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 11), desc="Levy C Curve"):
        generate_levy_curve(order)


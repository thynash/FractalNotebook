import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Cantor_Set"

def draw_cantor(ax, x, y, length, depth):
    if depth == 0:
        return
    ax.plot([x, x+length], [y, y], color='black', lw=2)
    if depth > 1:
        y -= 0.1
        draw_cantor(ax, x, y, length/3, depth-1)
        draw_cantor(ax, x + 2*length/3, y, length/3, depth-1)

def generate_cantor_set(order):
    plt.figure(figsize=(8,2))
    ax = plt.gca()
    draw_cantor(ax, 0, 1, 1, order)
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'cantor_set_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 11), desc="Cantor Set"):
        generate_cantor_set(order)


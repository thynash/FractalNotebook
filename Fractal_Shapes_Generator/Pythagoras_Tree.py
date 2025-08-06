import matplotlib.pyplot as plt
import numpy as np
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Pythagoras_tree"

def draw_tree(ax, p1, p2, depth):
    if depth == 0: return
    vec = np.array([p2[0]-p1[0], p2[1]-p1[1]])
    perp = np.array([-vec[1], vec[0]])
    p3 = p2 + perp
    p4 = p1 + perp
    ax.fill([p1[0], p2[0], p3[0], p4[0]],[p1[1],p2[1],p3[1],p4[1]],'lime')
    if depth > 1:
        draw_tree(ax, p4, p3, depth-1)
        draw_tree(ax, p3, p2 + vec + perp, depth-1)

def generate_pythagoras_tree(order):
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    draw_tree(ax, (0,0), (1,0), order)
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'pythagoras_tree_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 11), desc="Pythagoras Tree"):
        generate_pythagoras_tree(order)


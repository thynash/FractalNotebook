import matplotlib.pyplot as plt
import math, os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Dragon_Curve"

def dragon_curve(order):
    def turn_right(path): return [1-i for i in reversed(path)]
    path = []
    for _ in range(order):
        path = path + [0] + turn_right(path)
    return path

def generate_dragon_curve(order):
    plt.figure(figsize=(8,8))
    path = dragon_curve(order)
    x, y, angle = [0], [0], 0
    for turn in path:
        angle += math.pi/2 if turn else -math.pi/2
        x.append(x[-1] + math.cos(angle))
        y.append(y[-1] + math.sin(angle))
    plt.plot(x, y, color='purple')
    plt.axis('equal'); plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'dragon_curve_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 11), desc="Dragon Curve"):
        generate_dragon_curve(order)


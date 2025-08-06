import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

output_dir = "../Fractal_Shapes/Sierpinski_Carpet"

def sierpinski_carpet(order):
    size = 3 ** order
    img = np.ones((size, size), dtype=np.uint8) * 255
    def remove_center(x, y, s):
        if s == 1: return
        s3 = s // 3
        img[y+s3:y+2*s3, x+s3:x+2*s3] = 0
        for dx in range(3):
            for dy in range(3):
                if dx == dy == 1: continue
                remove_center(x + dx*s3, y + dy*s3, s3)
    remove_center(0, 0, size)
    return img

def generate_sierpinski_carpet(order):
    img = sierpinski_carpet(order)
    plt.figure(figsize=(8,8))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, f'sierpinski_carpet_order_{order}.png'), bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close()

if __name__ == "__main__":
    for order in tqdm(range(1, 8), desc="Sierpinski Carpet"):  # Memory needs limit order, 7 is 2187x2187 pixels
        generate_sierpinski_carpet(order)


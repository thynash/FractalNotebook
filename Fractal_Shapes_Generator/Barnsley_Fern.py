import numpy as np
import matplotlib.pyplot as plt

def generate_barnsley_fern(n_points=50000):
    x = y = 0
    xs, ys = [], []
    for _ in range(n_points):
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
    fig, ax = plt.subplots(figsize=(7, 10))
    ax.scatter(xs, ys, s=0.1, color='green')
    ax.axis('off')
    plt.tight_layout()
    return fig


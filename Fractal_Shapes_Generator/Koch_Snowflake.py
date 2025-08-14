import numpy as np
import matplotlib.pyplot as plt

koch_snowflake_description = r"""
### Koch Snowflake - Mathematical Construction

Given a line segment with endpoints \( p_1 \) and \( p_2 \):

1. Compute the division points:

$$
p_A = p_1 + \frac{1}{3}(p_2 - p_1), \quad 
p_C = p_1 + \frac{2}{3}(p_2 - p_1)
$$

2. Calculate the “peak” point \( p_B \) of the equilateral triangle constructed on the middle third:

$$
p_B = p_A + R_{\pi/3} (p_C - p_A), \quad \text{where} \quad
R_{\theta} = 
\begin{pmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{pmatrix}
$$

3. Replace the original segment \([p_1, p_2]\) by four new segments:

$$
[p_1, p_A], \quad [p_A, p_B], \quad [p_B, p_C], \quad [p_C, p_2]
$$

4. Apply this process recursively to each segment at the current iteration for the desired recursion order.

---

**Important properties:**

- The perimeter increases by a factor of \(\frac{4}{3}\) at each iteration, leading to an infinite perimeter in the limit.
- The enclosed area converges to a finite value.
- The fractal dimension \(D\) of the Koch Snowflake is:

$$
D = \frac{\log 4}{\log 3} \approx 1.2619
$$

This fractal exemplifies the beautiful interplay of simple geometric rules producing infinite complexity through recursion and self-similarity.
"""
def generate_koch_snowflake(order, zoom=1.0, ax=None):
    """
    Generate and plot Koch snowflake of given order, zooming by scaling the figure.
    Args:
        order (int): Recursion depth.
        zoom (float): Zoom factor that scales the fractal size (>0).
        ax (matplotlib.axes.Axes or None): Axis to plot on. If None, creates new.
    Returns:
        fig (matplotlib.figure.Figure): The matplotlib figure object.
    """
    BASE_SCALE = 10  # Fixed size; zoom multiplies this

    def koch_curve(p1, p2, order):
        if order == 0:
            return [tuple(p1), tuple(p2)]
        p1, p2 = np.array(p1), np.array(p2)
        delta = p2 - p1
        pA = p1 + delta / 3
        pC = p1 + 2 * delta / 3
        angle = np.pi / 3
        rot = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])
        pB = pA + np.dot(rot, pC - pA)
        return (
            koch_curve(p1, pA, order-1)[:-1] +
            koch_curve(pA, pB, order-1)[:-1] +
            koch_curve(pB, pC, order-1)[:-1] +
            koch_curve(pC, p2, order-1)
        )

    scale = BASE_SCALE * zoom
    initial_pts = [
        np.array([0, 0]),
        np.array([scale, 0]),
        np.array([scale/2, scale*np.sin(np.pi/3)]),
        np.array([0, 0])
    ]
    points = []
    for i in range(3):
        points.extend(koch_curve(initial_pts[i], initial_pts[i+1], order)[:-1])
    if points:
        points.append(points[0])
    x, y = zip(*points)
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure
    ax.fill(x, y, 'cyan', edgecolor='blue', linewidth=0.5)
    ax.axis('equal')
    ax.axis('off')
    return fig


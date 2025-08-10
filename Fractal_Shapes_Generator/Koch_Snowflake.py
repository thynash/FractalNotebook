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


def generate_koch_snowflake(order, scale=10, ax=None):
    """
    Generate and plot Koch snowflake of a given recursive order.

    Args:
        order (int): Recursion depth.
        scale (float): Size of the initial equilateral triangle.
        ax (matplotlib.axes.Axes or None): If None, a new figure and axis will be created.

    Returns:
        fig (matplotlib.figure.Figure): The Matplotlib figure containing the snowflake plot.
    """
    def koch_curve(p1, p2, order):
        if order == 0:
            return [tuple(p1), tuple(p2)]
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = p2 - p1
        pA = p1 + delta / 3
        pC = p1 + 2 * delta / 3
        angle = np.pi / 3  # 60 degrees
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        pB = pA + np.dot(rotation_matrix, pC - pA)
        return (
            koch_curve(p1, pA, order - 1)[:-1] +
            koch_curve(pA, pB, order - 1)[:-1] +
            koch_curve(pB, pC, order - 1)[:-1] +
            koch_curve(pC, p2, order - 1)
        )

    # Define vertices of the initial equilateral triangle
    initial_points = [
        np.array([0, 0]),
        np.array([scale, 0]),
        np.array([scale / 2, scale * np.sin(np.pi / 3)]),
        np.array([0, 0])  # Closing the triangle
    ]

    snowflake_points = []
    for i in range(3):
        snowflake_points.extend(koch_curve(initial_points[i], initial_points[i + 1], order)[:-1])
    if snowflake_points:
        snowflake_points.append(snowflake_points[0])  # Ensure closure

    x, y = zip(*snowflake_points)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure

    ax.fill(x, y, 'cyan', edgecolor='blue', linewidth=0.5)
    ax.axis('equal')
    ax.axis('off')

    return fig


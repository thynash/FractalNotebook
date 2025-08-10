import numpy as np
import matplotlib.pyplot as plt

def generate_koch_snowflake(order, scale=10, ax=None):
    """
    Generate and plot Koch snowflake of a given order.

    Args:
        order (int): Recursion order.
        scale (float): Size of initial triangle.
        ax (matplotlib axis or None): If None, creates a new figure/axis.

    Returns:
        fig (matplotlib.figure.Figure): The plotted figure object.
    """
    def koch_curve(p1, p2, order):
        if order == 0:
            return [tuple(p1), tuple(p2)]
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = p2 - p1
        pA = p1 + delta / 3
        pC = p1 + 2 * delta / 3
        angle = np.pi / 3
        rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        pB = pA + np.dot(rot, pC - pA)
        # Recursive step; only keep one copy of points at segment joins
        return (koch_curve(p1, pA, order-1)[:-1] +
                koch_curve(pA, pB, order-1)[:-1] +
                koch_curve(pB, pC, order-1)[:-1] +
                koch_curve(pC, p2, order-1))

    initial_pts = [
        np.array([0, 0]),
        np.array([scale, 0]),
        np.array([scale/2, scale * np.sin(np.pi / 3)]),
        np.array([0, 0])
    ]
    snowflake_points = []
    for i in range(3):
        snowflake_points.extend(koch_curve(initial_pts[i], initial_pts[i+1], order)[:-1])
    # Complete the loop
    if snowflake_points:
        snowflake_points.append(snowflake_points[0])
    x, y = zip(*snowflake_points)

    # Plotting
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig = ax.figure
    ax.fill(x, y, 'cyan', edgecolor='blue', linewidth=0.5)
    ax.axis('equal')
    ax.axis('off')
    return fig


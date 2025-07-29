import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# --- Configuration ---
# Directory to save the generated fractal images
output_dir = "../Fractal_Shapes/Sierpinski_triangle"

# --- Sierpinski Triangle Generation Function ---
def generate_sierpinski_triangle(order, p1=(0, 0), p2=(1, 0), p3=(0.5, 0.866)):
    """
    Generates and saves a single Sierpinski triangle image for a given order.

    Args:
        order (int): The recursion order of the triangle.
        p1, p2, p3 (tuple): The coordinates of the initial triangle's vertices.
    """
    def midpoint(p1, p2):
        """Calculates the midpoint between two points."""
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def draw_triangle(points, order):
        """Recursively draws the sub-triangles."""
        if order == 0:
            # Base case: draw a single filled triangle
            triangle = plt.Polygon(points, edgecolor='black', facecolor='magenta')
            plt.gca().add_patch(triangle)
        else:
            # Recursive step: calculate midpoints and draw three smaller triangles
            p1, p2, p3 = points
            mid12 = midpoint(p1, p2)
            mid23 = midpoint(p2, p3)
            mid31 = midpoint(p3, p1)
            draw_triangle([p1, mid12, mid31], order-1)
            draw_triangle([mid12, p2, mid23], order-1)
            draw_triangle([mid31, mid23, p3], order-1)

    # --- Plotting and Saving ---
    plt.figure(figsize=(8, 8))
    draw_triangle([p1, p2, p3], order)
    plt.axis('equal')
    plt.axis('off')
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the figure
    save_path = os.path.join(output_dir, f'sierpinski_triangle_order_{order}.png')
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close() # Close the figure to free up memory

# --- Main Execution Block ---
if __name__ == "__main__":
    # WARNING: Generating high orders (e.g., > 12) is computationally intensive
    # and may consume a large amount of memory and time.
    # The user's request for 10-100 is not feasible with this algorithm.
    # We will generate for a more practical range of 1 to 10.
    
    start_order = 1
    end_order = 10
    
    print(f"🔺 Generating Sierpinski triangles from order {start_order} to {end_order}...")
    
    # Use tqdm for a progress bar
    for order_num in tqdm(range(start_order, end_order + 1), desc="Generating Triangles"):
        generate_sierpinski_triangle(order=order_num)
        
    print(f"\n✅ Generation complete! Images saved in '{output_dir}'")


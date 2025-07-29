import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# --- Configuration ---
# Directory to save the generated fractal images
output_dir = "../Fractal_Shapes/koch_snowflakes"

# --- Koch Snowflake Generation Function ---
def generate_koch_snowflake(order, scale=10):
    """
    Generates and saves a single Koch snowflake image for a given order.

    Args:
        order (int): The recursion order of the snowflake.
        scale (int): The overall size of the initial triangle.
    """
    def koch_curve(p1, p2, order):
        """
        Recursively generates the points for a single Koch curve segment.
        """
        if order == 0:
            return [p1, p2]
        else:
            p1 = np.array(p1)
            p2 = np.array(p2)
            delta = p2 - p1
            
            # The three points that divide the segment into thirds
            pA = p1 + delta / 3
            pC = p1 + 2 * delta / 3

            # Calculate the tip of the equilateral triangle pointing outwards
            angle = np.pi / 3 # 60 degrees
            rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                        [np.sin(angle), np.cos(angle)]])
            pB = pA + np.dot(rotation_matrix, pC - pA)

            # Recursive calls for the four new segments
            # The '[:-1]' is used to avoid duplicating points between segments
            return koch_curve(p1, pA, order - 1)[:-1] + \
                   koch_curve(pA, pB, order - 1)[:-1] + \
                   koch_curve(pB, pC, order - 1)[:-1] + \
                   koch_curve(pC, p2, order - 1)

    # --- Main part of the generation function ---
    
    # Define the three corners of the initial equilateral triangle
    initial_points = [
        np.array([0, 0]),
        np.array([scale, 0]),
        np.array([scale/2, scale * np.sin(np.pi / 3)]),
        np.array([0, 0]) # Close the loop
    ]

    snowflake_points = []
    # Generate a Koch curve for each of the 3 sides of the initial triangle
    for i in range(3):
        snowflake_points.extend(koch_curve(initial_points[i], initial_points[i+1], order)[:-1])
    
    # Ensure the final point connects to the start
    if snowflake_points:
        snowflake_points.append(snowflake_points[0])

    # Unzip the points into x and y coordinates for plotting
    x, y = zip(*snowflake_points)

    # --- Plotting and Saving ---
    plt.figure(figsize=(8, 8))
    plt.fill(x, y, 'cyan', edgecolor='blue', linewidth=0.5)
    plt.axis('equal')
    plt.axis('off')
    # plt.title(f'Koch Snowflake (Order {order})') # Title can be disabled for cleaner images
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the figure
    save_path = os.path.join(output_dir, f'koch_snowflake_order_{order}.png')
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1, dpi=150)
    plt.close() # Close the figure to free up memory

# --- Main Execution Block ---
if __name__ == "__main__":
    # WARNING: Generating high orders (e.g., > 8) is computationally intensive
    # and may consume a large amount of memory and time.
    # The user's request for 1-100 is not feasible with this algorithm.
    # We will generate for a more practical range of 1 to 8.
    
    start_order = 1
    end_order = 10
    
    print(f"❄️ Generating Koch snowflakes from order {start_order} to {end_order}...")
    
    # Use tqdm for a progress bar
    for order_num in tqdm(range(start_order, end_order + 1), desc="Generating Snowflakes"):
        generate_koch_snowflake(order=order_num)
        
    print(f"\n✅ Generation complete! Images saved in '{output_dir}'")


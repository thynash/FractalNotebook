import streamlit as st
import matplotlib.pyplot as plt
import io
import sys
import os

# Ensure your generator package is on the path
fractal_dir = os.path.abspath(os.path.join('..', 'Fractal_Shapes_Generator'))
if fractal_dir not in sys.path:
    sys.path.insert(0, fractal_dir)

from Fractal_Shapes_Generator import (
    Mandelbrot as mandelbrot,
    Julia as julia,
    generate_koch_snowflake,
    generate_levy_curve,
    generate_pythagoras_tree,
    generate_sierpinski_triangle,
    generate_sierpinski_carpet,
    generate_dragon_curve,
    generate_cantor_set,
    generate_barnsley_fern,
    generate_hilbert_curve,
    generate_peano_curve,
    generate_newton_fractal
)

st.set_page_config(page_title="FractalNotebook", layout="wide")
st.title('FractalNotebook')

# Fractal display registry
fractals = {
    "Mandelbrot Set": {
        "generator": mandelbrot.generate_mandelbrot_set,
        "description": mandelbrot.mandelbrot_description,
        "params": ["max_iter", "zoom", "center_x", "center_y"]
    },
    "Julia Set": {
        "generator": julia.generate_julia_set,
        "description": julia.julia_description,
        "params": ["max_iter", "zoom", "center_x", "center_y", "c_real", "c_imag"]
    },
    "Koch Snowflake": {
        "generator": generate_koch_snowflake,
        "description": "The Koch Snowflake is constructed by recursively altering each straight edge into a spike. At each recursion level, edges become more intricate.",
        "params": ["order"]
    },
    "Levy C Curve": {
        "generator": generate_levy_curve,
        "description": "The Levy C curve is created by recursively bending lines at right angles, forming increasingly zig-zagged curves.",
        "params": ["order"]
    },
    "Pythagoras Tree": {
        "generator": generate_pythagoras_tree,
        "description": "The Pythagoras Tree is formed by growing squares recursively in a branching pattern.",
        "params": ["order"]
    },
    "Sierpinski Triangle": {
        "generator": generate_sierpinski_triangle,
        "description": "The Sierpinski Triangle is an iconic fractal built by recursively removing triangles, revealing self-similar gaps.",
        "params": ["order"]
    },
    "Sierpinski Carpet": {
        "generator": generate_sierpinski_carpet,
        "description": "The Sierpinski Carpet generalizes the triangle into a grid, recursively removing squares to create a woven fractal.",
        "params": ["order"]
    },
    "Dragon Curve": {
        "generator": generate_dragon_curve,
        "description": "The Dragon Curve is a recursive fold pattern resulting in a self-similar zig-zag shape.",
        "params": ["order"]
    },
    "Cantor Set": {
        "generator": generate_cantor_set,
        "description": "The Cantor Set is formed by iteratively removing the central third of every segment.",
        "params": ["order"]
    },
    "Barnsley Fern": {
        "generator": generate_barnsley_fern,
        "description": "The Barnsley Fern uses random affine transforms to mimic fern leaf growth.",
        "params": ["n_points"]
    },
    "Hilbert Curve": {
        "generator": generate_hilbert_curve,
        "description": "The Hilbert Curve is a space-filling path that visits every cell of a grid via recursive turns.",
        "params": ["order"]
    },
    "Peano Curve": {
        "generator": generate_peano_curve,
        "description": "The Peano Curve recursively fills a grid, visiting every cell.",
        "params": ["order"]
    },
    "Newton Fractal": {
        "generator": generate_newton_fractal,
        "description": "The Newton Fractal visualizes the basins of attraction for Newton's method applied to complex polynomials.",
        "params": ["order"]
    }
}

selection = st.selectbox(
    'Fractal:',
    list(fractals.keys()),
    key='fractal_selector'
)

# Column layout for controls and image
iterations_col, zoom_col, center_col, position_col = st.columns([1, 1, 5, 2])

# Parameters dictionary to collect controls dynamically
params = {}

with iterations_col:
    if "max_iter" in fractals[selection]["params"]:
        params["max_iter"] = st.slider('Iterations', 50, 1000, 256, 50)
    if "order" in fractals[selection]["params"]:
        params["order"] = st.slider('Order', 1, 10, 5)

with zoom_col:
    if "zoom" in fractals[selection]["params"]:
        params["zoom"] = st.slider('Zoom (1x–100x)', 1, 100, 1)

with position_col:
    if "center_x" in fractals[selection]["params"]:
        params["center_x"] = st.slider('Center X', -2.0, 2.0, 0.0, step=0.01)
    if "center_y" in fractals[selection]["params"]:
        params["center_y"] = st.slider('Center Y', -2.0, 2.0, 0.0, step=0.01)
    if "c_real" in fractals[selection]["params"]:
        params["c_real"] = st.slider('Julia c (Real)', -1.5, 1.5, -0.8, 0.01)
    if "c_imag" in fractals[selection]["params"]:
        params["c_imag"] = st.slider('Julia c (Imag)', -1.5, 1.5, 0.156, 0.01)
    if "n_points" in fractals[selection]["params"]:
        params["n_points"] = st.slider('Num Points', 5_000, 100_000, 50_000, 5_000)

with center_col:
    RECT_WIDTH = 700
    RECT_HEIGHT = 400
    ASPECT = RECT_WIDTH / RECT_HEIGHT

    def zoom_bounds(center_x, center_y, base_span, aspect_ratio, zoom):
        width = base_span / zoom
        height = width / aspect_ratio
        xmin = center_x - width / 2
        xmax = center_x + width / 2
        ymin = center_y - height / 2
        ymax = center_y + height / 2
        return xmin, xmax, ymin, ymax

    fig, ax = plt.subplots(figsize=(7, 4), dpi=100)

    # Dynamic generator dispatcher
    img = None
    if selection == "Mandelbrot Set":
        xmin, xmax, ymin, ymax = zoom_bounds(params["center_x"], params["center_y"], 3.0, ASPECT, params["zoom"])
        img = fractals[selection]["generator"](xmin, xmax, ymin, ymax, RECT_WIDTH, RECT_HEIGHT, params["max_iter"])
        ax.imshow(img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
        ax.axis('off')
    elif selection == "Julia Set":
        xmin, xmax, ymin, ymax = zoom_bounds(params["center_x"], params["center_y"], 4.0, ASPECT, params["zoom"])
        img = fractals[selection]["generator"](complex(params["c_real"], params["c_imag"]), xmin, xmax, ymin, ymax, RECT_WIDTH, RECT_HEIGHT, params["max_iter"])
        ax.imshow(img, cmap='cool', extent=(xmin, xmax, ymin, ymax))
        ax.axis('off')
    elif selection == "Barnsley Fern":
        x, y = fractals[selection]["generator"](params["n_points"])
        ax.scatter(x, y, s=0.1, color='green')
        ax.axis('off')
    elif selection == "Newton Fractal":
        img = fractals[selection]["generator"](order=params["order"])
        ax.imshow(img, extent=(-1.5,1.5,-1.5,1.5), cmap='hsv')
        ax.axis('off')
    elif selection in ["Koch Snowflake", "Levy C Curve", "Pythagoras Tree", "Sierpinski Triangle", "Sierpinski Carpet", "Dragon Curve", "Cantor Set", "Hilbert Curve", "Peano Curve"]:
        fractals[selection]["generator"](ax, params["order"])
        ax.axis('off')
    else:
        st.warning("Fractal not implemented yet.")

    plt.tight_layout(pad=0)
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    st.image(buf, width=RECT_WIDTH)
    st.markdown(fractals[selection]["description"])


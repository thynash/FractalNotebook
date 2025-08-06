import streamlit as st
import matplotlib.pyplot as plt
import io
import sys
import os

from Fractal_Shapes_Generator import Mandelbrot as mandelbrot
from Fractal_Shapes_Generator import Julia as julia

st.set_page_config(page_title="FractalNotebook", layout="wide")
st.title('FractalNotebook')

selection = st.selectbox(
    'Fractal:',
    ['Mandelbrot Set', 'Julia Set'],
    key='fractal_selector'
)

# Adjusted column proportions for playground/controls
iterations_col, zoom_col, center_col, position_col = st.columns([1, 1, 5, 2])

with iterations_col:
    st.markdown("#### Iterations")
    max_iter = st.slider('Iterations', 50, 1000, 256, 50, key='iter')

with zoom_col:
    st.markdown("#### Zoom")
    zoom = st.slider('Zoom (1x–100x)', 1, 100, 1, key='zoom')

with position_col:
    st.markdown("#### Position Controls")
    if selection == 'Mandelbrot Set':
        center_x = st.slider('Center X', -2.0, 1.0, -0.5, step=0.01)
        center_y = st.slider('Center Y', -1.5, 1.5, 0.0, step=0.01)
    elif selection == 'Julia Set':
        c_real = st.slider('Julia c (Real)', -1.5, 1.5, -0.8, 0.01)
        c_imag = st.slider('Julia c (Imag)', -1.5, 1.5, 0.156, 0.01)
        center_x = st.slider('Center X', -2.0, 2.0, 0.0, step=0.01)
        center_y = st.slider('Center Y', -2.0, 2.0, 0.0, step=0.01)

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

    if selection == 'Mandelbrot Set':
        xmin, xmax, ymin, ymax = zoom_bounds(center_x, center_y, 3.0, ASPECT, zoom)
        img = mandelbrot.generate_mandelbrot_set(xmin, xmax, ymin, ymax, RECT_WIDTH, RECT_HEIGHT, max_iter)
        fig, ax = plt.subplots(figsize=(7, 4), dpi=100)
        ax.imshow(img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
        ax.axis('off')
        plt.tight_layout(pad=0)
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        buf.seek(0)
        st.image(buf, width=RECT_WIDTH)
        st.markdown(mandelbrot.mandelbrot_description)
    elif selection == 'Julia Set':
        xmin, xmax, ymin, ymax = zoom_bounds(center_x, center_y, 4.0, ASPECT, zoom)
        img = julia.generate_julia_set(complex(c_real, c_imag), xmin, xmax, ymin, ymax, RECT_WIDTH, RECT_HEIGHT, max_iter)
        fig, ax = plt.subplots(figsize=(7, 4), dpi=100)
        ax.imshow(img, cmap='cool', extent=(xmin, xmax, ymin, ymax))
        ax.axis('off')
        plt.tight_layout(pad=0)
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        buf.seek(0)
        st.image(buf, width=RECT_WIDTH)
        st.markdown(julia.julia_description)


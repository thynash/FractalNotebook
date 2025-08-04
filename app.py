import streamlit as st
from PIL import Image
import os

# Directory where fractal images are saved
IMAGE_DIR = 'Fractal_Shapes'

# Load images
def load_image(name):
    return Image.open(os.path.join(IMAGE_DIR, name))

# Map fractal types to filenames
fractals = {
    'Mandelbrot Set': 'Mandelbrot.png',
    'Julia Set': 'Julia.png',
#    'Koch Snowflake': 'koch_snowflake_order_4.png',
#    'Sierpinski Triangle': 'sierpinski_triangle_order_6.png'
}

# Streamlit UI
st.title('FractalNotebook Viewer')

selection = st.selectbox('Select Fractal Geometry:', list(fractals.keys()))

if selection:
    st.image(load_image(fractals[selection]), caption=selection, use_container_width=True)


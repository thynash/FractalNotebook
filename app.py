import streamlit as st
import matplotlib.pyplot as plt

# Add your fractal package to sys.path
from Fractal_Shapes_Generator import Mandelbrot as mandelbrot
from Fractal_Shapes_Generator import Julia as julia
def zoom_bounds(center_x, center_y, base_span, zoom):
    span = base_span / zoom  # base_span: width/height at zoom 1
    xmin = center_x - span/2
    xmax = center_x + span/2
    ymin = center_y - span/2
    ymax = center_y + span/2
    return xmin, xmax, ymin, ymax

st.title('FractalNotebook Viewer (Zoomable Mandelbrot & Julia)')

selection = st.sidebar.selectbox(
    'Choose Fractal Geometry:',
    ['Mandelbrot Set', 'Julia Set'])

if selection == 'Mandelbrot Set':
    st.markdown(mandelbrot.mandelbrot_description)
    center_x = st.slider('Center X', -2.0, 1.0, -0.5, step=0.01)
    center_y = st.slider('Center Y', -1.5, 1.5, 0.0, step=0.01)
    zoom = st.slider('Zoom (1x - 100x)', 1, 100, 1)
    max_iter = st.slider('Iterations', 50, 1000, 256, 50)

    xmin, xmax, ymin, ymax = zoom_bounds(center_x, center_y, base_span=3.0, zoom=zoom)
    mandelbrot_img = mandelbrot.generate_mandelbrot_set(xmin, xmax, ymin, ymax, 600, 600, max_iter)

    fig, ax = plt.subplots()
    ax.imshow(mandelbrot_img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    ax.set_title(f"Mandelbrot (Zoom: {zoom}x, Center: {center_x}, {center_y})")
    ax.axis('off')
    st.pyplot(fig)

elif selection == 'Julia Set':
    st.markdown(julia.julia_description)
    c_real = st.slider('Julia Parameter: Real Part of c', -1.5, 1.5, -0.8, 0.01)
    c_imag = st.slider('Julia Parameter: Imaginary Part of c', -1.5, 1.5, 0.156, 0.01)
    center_x = st.slider('Center X', -2.0, 2.0, 0.0, step=0.01)
    center_y = st.slider('Center Y', -2.0, 2.0, 0.0, step=0.01)
    zoom = st.slider('Zoom (1x - 100x)', 1, 100, 1)
    max_iter = st.slider('Iterations', 50, 1000, 256, 50)

    xmin, xmax, ymin, ymax = zoom_bounds(center_x, center_y, base_span=4.0, zoom=zoom)
    julia_img = julia.generate_julia_set(complex(c_real, c_imag), xmin, xmax, ymin, ymax, 600, 600, max_iter)

    fig, ax = plt.subplots()
    ax.imshow(julia_img, cmap='cool', extent=(xmin, xmax, ymin, ymax))
    ax.set_title(f"Julia (c = {c_real} + {c_imag}i, Zoom: {zoom}x, Center: {center_x}, {center_y})")
    ax.axis('off')
    st.pyplot(fig)


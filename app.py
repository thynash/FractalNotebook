import streamlit as st
import matplotlib.pyplot as plt

# Import your custom modules as regular modules thanks to __init__.py
from Fractal_Shapes_Generator import Mandelbrot, Julia

st.title('FractalNotebook Viewer')

selection = st.sidebar.selectbox('Choose Fractal Geometry:', ['Mandelbrot Set', 'Julia Set'])

if selection == 'Mandelbrot Set':
    st.markdown(Mandelbrot.mandelbrot_description)
    max_iter = st.slider('Iterations', 50, 1000, 250, 50)
    mandelbrot_img = Mandelbrot.generate_mandelbrot_set(-2.0, 1.0, -1.5, 1.5, 500, 350, max_iter)
    fig, ax = plt.subplots()
    ax.imshow(mandelbrot_img, cmap='hot', extent=(-2, 1, -1.5, 1.5))
    ax.axis('off')
    st.pyplot(fig)

elif selection == 'Julia Set':
    st.markdown(Julia.julia_description)
    c_real = st.slider('Real part of c', -1.5, 1.5, -0.8, 0.01)
    c_imag = st.slider('Imaginary part of c', -1.5, 1.5, 0.156, 0.01)
    max_iter = st.slider('Iterations', 50, 1000, 250, 50)
    julia_img = Julia.generate_julia_set(complex(c_real, c_imag), -2.0, 2.0, -2.0, 2.0, 500, 500, max_iter)
    fig, ax = plt.subplots()
    ax.imshow(julia_img, cmap='cool', extent=(-2, 2, -2, 2))
    ax.axis('off')
    st.pyplot(fig)


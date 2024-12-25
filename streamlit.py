import streamlit as st
from Fractals import Mandelbrot, Julia, BurningShip, Tricorn
import matplotlib.pyplot as plt

st.title("Fractals")
st.write("This is a simple visualization of different fractals. It is not perfect and quite slow, but it works.")

option = st.selectbox(
    'Which fractal would you like to see?',
    ('Mandelbrot', 'Julia', 'Burning Ship', 'Tricorn'),
    index=None,
    placeholder='Choose a fractal',
)

max_itter = int(st.number_input('Choose the number of iterations for fractal generation. Aim for a balance between detail and speed. Recommended range: 100-1000 iterations.',
                               min_value=1, value=100, step=10))

# Create fractal based on the selection
if option == 'Mandelbrot':
    mandelbrot = Mandelbrot(xmin=-2, xmax=1, ymin=-1, ymax=1, width=1000, height=1000, max_iter=max_itter)
    fig, ax = plt.subplots()
    mandelbrot.display_fractal(ax)
    st.pyplot(fig)

elif option == 'Julia':
    julia_set = Julia(h_range=1200, w_range=1200, max_iter=max_itter)
    fig, ax = plt.subplots()
    julia_set.draw_julia(ax)
    st.pyplot(fig)

elif option == 'Burning Ship':
    burning_ship = BurningShip(x=-2, y=-2, num_iterations=max_itter)
    fig, ax = plt.subplots()
    burning_ship.display_burning(ax)
    st.pyplot(fig)

elif option == 'Tricorn':
    tricorn = Tricorn(width=1200, height=1200, max_iter=max_itter)
    fig, ax = plt.subplots()
    tricorn.display_fractal(ax)
    st.pyplot(fig)

# Placeholder for future fractals
elif option == 'Multibrot':
    st.write("Multibrot fractal not implemented yet.")
    fig, ax = plt.subplots()
    st.pyplot(fig)

elif option == 'Bifurcation':
    st.write("Bifurcation fractal not implemented yet.")
    fig, ax = plt.subplots()
    st.pyplot(fig)

elif option == 'Newton':
    st.write("Newton fractal not implemented yet.")
    fig, ax = plt.subplots()
    st.pyplot(fig)

elif option == 'Buddhabrot':
    st.write("Buddhabrot fractal not implemented yet.")
    fig, ax = plt.subplots()
    st.pyplot(fig)
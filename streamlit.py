import streamlit as st
from Fractals import Mandelbrot, Julia, BurningShip, Tricorn
st.set_option('deprecation.showPyplotGlobalUse', False)

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

# Remove the deprecated option setting
# st.set_option('deprecation.showPyplotGlobalUse', False)

# Create fractal based on the selection
if option == 'Mandelbrot':
    mandelbrot = Mandelbrot(xmin=-2, xmax=1, ymin=-1, ymax=1, width=1000, height=1000, max_iter=max_itter)
    mandelbrot.display_fractal()
    st.pyplot()

elif option == 'Julia':
    julia_set = Julia(h_range=1200, w_range=1200, max_iter=max_itter)
    julia_set.draw_julia()
    st.pyplot()

elif option == 'Burning Ship':
    burning_ship = BurningShip(x=-2, y=-2, num_iterations=max_itter)
    burning_ship.display_burning()
    st.pyplot()

elif option == 'Tricorn':
    tricorn = Tricorn(width=1200, height=1200, max_iter=max_itter)
    tricorn.display_fractal()
    st.pyplot()

# Placeholder for future fractals
elif option == 'Multibrot':
    st.write("Multibrot fractal not implemented yet.")
    st.pyplot()

elif option == 'Bifurcation':
    st.write("Bifurcation fractal not implemented yet.")
    st.pyplot()

elif option == 'Newton':
    st.write("Newton fractal not implemented yet.")
    st.pyplot()

elif option == 'Buddhabrot':
    st.write("Buddhabrot fractal not implemented yet.")
    st.pyplot()

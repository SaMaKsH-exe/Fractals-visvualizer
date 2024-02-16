import streamlit as st
from Fractals import Mandelbrot, Julia, BurningShip,Tricorn
import matplotlib.pyplot as plt

st.title("Fractals")
st.write("This is simple visualisations of different fractals")


option = st.selectbox(
    'Which fractal would you like to see?',
    ('Mandelbrot', 'Julia', 'Burning Ship', 'Tricorn', 'Multibrot', 'Bifurcation', 'Newton', 'Buddhabrot'),
    index=None,
    placeholder='Choose a fractal',
)

st.set_option('deprecation.showPyplotGlobalUse', False)

if option == 'Mandelbrot':
    mandalbrot = Mandelbrot( xmin=-2, xmax=1, ymin=-1, ymax=1, width=1000, height=1000, max_iter=256)
    mandalbrot.display_fractal()
    st.pyplot()
    
elif option == 'Julia':
    julia_set = Julia(h_range=1000, w_range=1000, max_iter=100)
    julia_set.draw_julia()
    st.pyplot()

elif option == 'Burning Ship':
    burning_ship = BurningShip(x=-2, y=-2, num_iterations=100)
    burning_ship.display_burning()
    st.pyplot()

elif option == 'Tricorn':
    tricorn = Tricorn(width=1200, height=1200, max_iter=100)
    tricorn.display_fractal()
    st.pyplot()

elif option == 'Multibrot':
    st.write("Multibrot Set")
    st.pyplot()

elif option == 'Bifurcation':
    st.write("Bifurcation Set")
    st.pyplot()

elif option == 'Newton':
    st.write("Newton Set")
    st.pyplot()

elif option == 'Buddhabrot':
    st.write("Buddhabrot Set")
    st.pyplot()


import streamlit as st
from Fractals import Mandelbrot, Julia, BurningShip,Tricorn


st.title("Fractals")
st.write("This is simple visualisations of different fractals, it is not perfect and quote slow, but it hey it works.")


option = st.selectbox(
    'Which fractal would you like to see?',
    ('Mandelbrot', 'Julia', 'Burning Ship', 'Tricorn', 'Multibrot', 'Bifurcation', 'Newton', 'Buddhabrot'),
    index=None,
    placeholder='Choose a fractal',
)

max_itter = int(st.number_input('Choose the number of iterations for fractal generation. Aim for a balance between detail and speed. Recommended range: 100-1000 iterations.', min_value=1, value=100, step=10      ))

st.set_option('deprecation.showPyplotGlobalUse', False)



if option == 'Mandelbrot':
    mandalbrot = Mandelbrot( xmin=-2, xmax=1, ymin=-1, ymax=1, width=1000, height=1000, max_iter= max_itter)
    mandalbrot.display_fractal()
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

elif option == 'Multibrot':
    st.pyplot()

elif option == 'Bifurcation':
    st.pyplot()

elif option == 'Newton':
    st.pyplot()

elif option == 'Buddhabrot':
    st.pyplot()


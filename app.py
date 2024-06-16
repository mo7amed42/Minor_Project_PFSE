import streamlit as st
from app_module import calculate_beam_deflection
import matplotlib.pyplot as plt
import numpy as np

st.title("Beam Deflection Calculator")

# User inputs
length = st.number_input("Beam Length (m)", min_value=1.0, value=10.0)
load = st.number_input("Uniform Load (N/m)", min_value=1.0, value=5000.0)
youngs_modulus = st.number_input("Young's Modulus (Pa)", min_value=1e9, value=210e9)
moment_of_inertia = st.number_input("Moment of Inertia (m^4)", min_value=1e-6, value=0.0001)

if st.button("Calculate Deflection"):
    deflections = calculate_beam_deflection(length, load, youngs_modulus, moment_of_inertia)
    
    st.write(f"Deflections at supports: {deflections}")
    
    # Visualization
    fig, ax = plt.subplots()
    x = np.linspace(0, length, 100)
    y = np.interp(x, [0, length], deflections)
    ax.plot(x, y)
    ax.set_title('Beam Deflection Curve')
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Deflection (m)')
    st.pyplot(fig)
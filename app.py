# app.py

import streamlit as st
#import numpy as np
import matplotlib.pyplot as plt
from app_module import create_beam_model, analyze_beam

# Streamlit app
st.title("Simply Supported Beam Analysis")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # User inputs
    length = st.number_input("Beam Length (m)", min_value=0.1, value=5.0, step=0.1)
    load = st.number_input("Point Load (N)", value=-1000.0, step=100.0)
    load_position = st.number_input("Load Position (m)", min_value=0.0, max_value=length, value=2.5, step=0.1)
    E = st.number_input("Young's Modulus (Pa)", value=210e9, step=1e9)
    nu = st.number_input("Poisson's Ratio", value=0.3, step=0.05)
    rho = st.number_input("Density (kg/m^3)", value=7850, step=100)
    Iy = st.number_input("Moment of Inertia Iy (m^4)", min_value=1e-9, value=100e-6, step=1e-6)
    Iz = st.number_input("Moment of Inertia Iz (m^4)", min_value=1e-9, value=100e-6, step=1e-6)
    J = st.number_input("Torsional Constant J (m^4)", min_value=1e-9, value=0.1e-6, step=1e-7)
    A = st.number_input("Cross-Sectional Area (m^2)", min_value=1e-9, value=1e-4, step=1e-5)

if st.button("Analyze Beam"):
    if Iy <= 0 or Iz <= 0 or J <= 0 or A <= 0:
        st.error("Moment of Inertia, Torsional Constant, and Cross-Sectional Area must be greater than zero.")
    else:
        model = create_beam_model(length, load, load_position, E, nu, rho, Iy, Iz, J, A)
        moments = analyze_beam(model)

        positions = moments[0]
        bending_moments = moments[1]

        # Plot results
        with col2:
            st.header("Results")
            fig, ax = plt.subplots()
            ax.plot(positions, bending_moments, label='Bending Moment Mz')
            ax.set_xlabel('Position along the beam (m)')
            ax.set_ylabel('Bending Moment (Nm)')
            ax.legend()
            st.pyplot(fig)

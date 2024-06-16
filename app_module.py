import streamlit as st
import matplotlib.pyplot as plt
from app import create_beam, plot_bending_moment

# Title and description
st.title("Simply Supported Beam Analysis")
st.write("""
    This application allows you to analyze a simply supported beam with a point load.
    Provide the beam length, load magnitude, and load position to get the analysis results.
""")

# Input parameters
length = st.number_input("Beam Length (m)", min_value=1.0, value=10.0)
load = st.number_input("Load Magnitude (N)", min_value=1.0, value=1000.0)
load_position = st.number_input("Load Position (m)", min_value=0.0, max_value=length, value=5.0)

# Button to run analysis
if st.button("Run Analysis"):
    with st.spinner("Running analysis..."):
        model = create_beam(length, load, load_position)

        # Plot bending moment diagram
        fig, ax = plt.subplots()
        plot_bending_moment(model)
        st.pyplot(fig)
    
    st.success("Analysis complete!")

# To run this app, use the command `streamlit run app.py` in your terminal.

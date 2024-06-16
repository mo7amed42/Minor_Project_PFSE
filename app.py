import numpy as np
import matplotlib.pyplot as plt
from PyNite import FEModel3D

def create_beam(length, load, load_position):
    """
    Create a simply supported beam with a point load.

    Parameters:
    length (float): The length of the beam.
    load (float): The magnitude of the point load.
    load_position (float): The position of the point load from the left end of the beam.

    Returns:
    model (FEModel3D): The finite element model of the beam.
    """



    # Create a new finite element model
    model = FEModel3D()

        # Define material properties and section properties
    E = 210e9      # Young's modulus in Pascals (N/m^2)
    nu = 0.3       # Poisson's ratio
    rho = 7850     # Density in kg/m^3 (common value for steel)
    G = E / (2 * (1 + nu))  # Shear modulus in Pascals (N/m^2)
    Iy = 100e-6    # Moment of inertia about the y-axis in m^4
    Iz = 100e-6    # Moment of inertia about the z-axis in m^4
    J = 0.1e-6     # Torsional constant in m^4
    A = 1e-4       # Cross-sectional area in m^2
    
    model.add_material("Steel", E, G, nu, rho)
    
    # Add nodes (supports)
    model.add_node('N1', 0, 0, 0)
    model.add_node('N2', length, 0, 0)

    # Add a beam element between the nodes
    model.add_member('M1', 'N1', 'N2', "Steel", Iy, Iz, J, A)

    
    # Add supports (simply supported)
    model.def_support('N1', True, True, True, True, False, False)
    model.def_support('N2', False, True, True, False, False, False)
    
    model.add_load_combo('LC1', {"D": 1.25, "L": 1.5})
    
    # Add a point load at the specified position
    model.add_member_pt_load(Member='M1', Direction='Fy', P=load, x=load_position,case="D")
    model.analyze(check_statics=True)
        
    return model
    

def plot_bending_moment(model):
    """
    Plot the bending moment diagram of the beam using matplotlib.

    Parameters:
    model (FEModel3D): The finite element model of the beam.
    """
    # Get bending moments along the beam member
    member = model.Members['M1']
    moments = member.plot_moment(Direction="Mz", combo_name='LC1', n_points=100)

    # Extract distances and bending moments for plotting
    distances = [point[0] for point in moments]
    bending_moments = [point[1] for point in moments]

    # Plotting the bending moment diagram
    plt.figure(figsize=(10, 6))
    plt.plot(distances, bending_moments, marker='o', linestyle='-', color='b')
    plt.xlabel('Distance (m)')
    plt.ylabel('Bending Moment (Nm)')
    plt.title('Bending Moment Diagram')
    plt.grid(True)
    plt.tight_layout()

    return plt
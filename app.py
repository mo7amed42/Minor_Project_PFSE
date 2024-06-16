import numpy as np
from PyNite import FEModel3D, Visualization

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

    # Define material properties and section properties
    E = 210e9      # Young's modulus in Pascals (N/m^2)
    nu = 0.3       # Poisson's ratio
    rho = 7850     # Density in kg/m^3 (common value for steel)
    G = E / (2 * (1 + nu))  # Shear modulus in Pascals (N/m^2)
    Iy = 100e-6    # Moment of inertia about the y-axis in m^4
    Iz = 100e-6    # Moment of inertia about the z-axis in m^4
    J = 0.1e-6     # Torsional constant in m^4
    A = 1e-4       # Cross-sectional area in m^2

    # Create a new finite element model
    model = FEModel3D()

    # Add a material to the model
    model.add_material("Steel", E, G, nu, rho)
    
    # Add nodes (supports)
    model.add_node('N1', 0, 0, 0)
    model.add_node('N2', length, 0, 0)

    # Add a beam element between the nodes
    model.add_member('M1', 'N1', 'N2', "Steel", Iy, Iz, J, A)
  
    # Add supports (simply supported)
    model.def_support('N1', True, True, True, False, False, False)
    model.def_support('N2', True, True, True, False, False, False)
    
    # Add a point load at the specified position
    model.add_member_pt_load('M1', 'Fy', load, load_position)

    # Analyze the model
    model.analyze()

    return model

def plot_bending_moment(model):
    """
    Plot the bending moment diagram of the beam.

    Parameters:
    model (FEModel3D): The finite element model of the beam.
    """
    Visualization.RenderModel(model, deformed_shape=True, deformed_scale=100, render_loads=True)

# Add unit tests using pytest
#def test_create_beam():
#    length = 10  # Example length in meters
#    load = 1000  # Example load in Newtons
#    load_position = 5  # Example load position in meters from the left support

#    model = create_beam(length, load, load_position)
    
 #   assert len(model.Nodes) == 2
 #   assert len(model.Members) == 1
 #   assert model.Nodes['N1'].X == 0
 #   assert model.Nodes['N2'].X == length

# You can add more tests to check for the correct reactions, displacements, etc.

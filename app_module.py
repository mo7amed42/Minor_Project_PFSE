import numpy as np
#from PyNite import FEModel3D, Beam3D
from PyNite import FEModel3D

def calculate_beam_deflection(length, load, youngs_modulus, moment_of_inertia):
    # Create a new finite element model
    model = FEModel3D()
    
    # Add nodes (supports)
    model.add_node('N1', 0, 0, 0)
    model.add_node('N2', length, 0, 0)
    
    # Add beam element
    model.add_member('Beam', 'N1', 'N2', youngs_modulus, moment_of_inertia, moment_of_inertia, 1e-6, 1e-6, 1e-6)
    
    # Add supports
    model.def_support('N1', True, True, True, True, True, True)
    model.def_support('N2', False, True, True, True, True, True)
    
    # Add load
    model.add_member_dist_load('Beam', 'Fy', load, load)
    
    # Analyze the model
    model.Analyze()
    
    # Get deflection results
    deflections = [model.Nodes('N1').DY, model.Nodes('N2').DY]
    return deflections
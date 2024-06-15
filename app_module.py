import numpy as np
#from PyNite import FEModel3D, Beam3D
from PyNite.FEModel3D import FEModel3D

def calculate_beam_deflection(length, load, youngs_modulus, moment_of_inertia):
    # Create a new finite element model
    model = FEModel3D()
    
    # Add nodes (supports)
    model.AddNode('N1', 0, 0, 0)
    model.AddNode('N2', length, 0, 0)
    
    # Add beam element
    model.AddMember('Beam', 'N1', 'N2', youngs_modulus, moment_of_inertia, moment_of_inertia, 1e-6, 1e-6, 1e-6)
    
    # Add supports
    model.DefineSupport('N1', True, True, True, True, True, True)
    model.DefineSupport('N2', False, True, True, True, True, True)
    
    # Add load
    model.AddMemberDistLoad('Beam', 'Fy', load, load)
    
    # Analyze the model
    model.Analyze()
    
    # Get deflection results
    deflections = [model.GetNode('N1').DY, model.GetNode('N2').DY]
    return deflections
# beam_analysis.py

from PyNite import FEModel3D

def create_beam_model(length, load, load_position, E, nu, rho, Iy, Iz, J, A):
    # Create a new finite element model
    model = FEModel3D()
    
    G = E / (2 * (1 + nu))  # Shear modulus in Pascals (N/m^2)
    
    # Add material
    model.add_material("Steel", E, G, nu, rho)
    
    # Add nodes (supports)
    model.add_node('N1', 0, 0, 0)
    model.add_node('N2', length, 0, 0)
    
    # Add a beam element between the nodes
    model.add_member('M1', 'N1', 'N2', "Steel", Iy, Iz, J, A)
    
    # Add supports (simply supported)
    model.def_support('N1', True, True, True, True, False, False)
    model.def_support('N2', False, True, True, False, False, False)
    
    # Add load combo
    model.add_load_combo('LC1', {"D": 1.25, "L": 1.5})
    
    # Add a point load at the specified position
    model.add_member_pt_load(Member='M1', Direction='Fy', P=load, x=load_position, case="D")
    
    return model

def analyze_beam(model):
    model.analyze(check_statics=True)
    moment = model.Members['M1'].moment_array("Mz", 100, "LC1")
    return moment

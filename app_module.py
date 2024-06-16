from PyNite import FEModel3D

def calculate_beam_deflection(length, load, youngs_modulus, moment_of_inertia):
    try:
        # Create a new finite element model
        model = FEModel3D()
        
        # Define Poisson's ratio and density for steel
        poisson_ratio = 0.3
        density = 7850  # kg/m^3, typical density of steel
        
        # Add material properties directly to the model
        model.add_material('Steel', E=youngs_modulus, G=youngs_modulus / (2 * (1 + poisson_ratio)), nu=poisson_ratio, rho=density)
        
        # Add nodes (supports)
        model.add_node('N1', 0, 0, 0)
        model.add_node('N2', length, 0, 0)
        
        # Cross-sectional area
        area = 0.01  # m^2 (example value, adjust as needed)
        
        # Add beam element
        model.add_member('Beam', 'N1', 'N2', 'Steel', Iy=moment_of_inertia, Iz=moment_of_inertia, J=1e-6, A=area)
        
        # Define supports
        model.def_support('N1', 'UX', True)
        model.def_support('N1', 'UY', True)
        model.def_support('N1', 'UZ', True)
        model.def_support('N1', 'RX', True)
        model.def_support('N1', 'RY', True)
        model.def_support('N1', 'RZ', False)
        
        model.def_support('N2', 'UX', False)
        model.def_support('N2', 'UY', True)
        model.def_support('N2', 'UZ', False)
        model.def_support('N2', 'RX', False)
        model.def_support('N2', 'RY', False)
        model.def_support('N2', 'RZ', False)
        
        # Add load
        model.add_member_dist_load('Beam', 'Fy', load, load)
        
        # Analyze the model
        model.analyze()
        
        # Get deflection results
        deflections = [model.Nodes['N1'].DY, model.Nodes['N2'].DY]
        return deflections
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
length = 5.0  # meters
load = -1000  # N/m (negative sign indicates a downward load)
youngs_modulus = 210e9  # Pa
moment_of_inertia = 0.0001  # m^4

print(calculate_beam_deflection(length, load, youngs_modulus, moment_of_inertia))

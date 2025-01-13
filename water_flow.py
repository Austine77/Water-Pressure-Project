def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column.
    h = t + (3w / 4)
    """
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity on the water column.
    P = (ρ * g * h) / 1000
    """
    rho = 998.2  # Density of water in kg/m³
    g = 9.80665  # Acceleration due to gravity in m/s²
    return (rho * g * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the pressure loss due to friction in the pipe.
    P = -f * L * ρ * v² / (2000 * d)
    """
    rho = 998.2  # Density of water in kg/m³
    return (-friction_factor * pipe_length * rho * fluid_velocity**2) / (2000 * pipe_diameter)

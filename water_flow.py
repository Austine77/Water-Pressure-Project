# water_flow.py

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # (m/s^2)
WATER_DENSITY = 998.2  # (kg/m^3)
WATER_DYNAMIC_VISCOSITY = 0.0010016  # (Pa.s)

# Function to calculate water column height
def water_column_height(tower_height, tank_height):
    return tower_height - tank_height

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(water_height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height) / 1000  # kPa

# Function to calculate pressure loss from pipe
def pressure_loss_from_pipe(diameter, length, friction, velocity):
    return (-friction * (length / diameter) * velocity**2) / 2000  # kPa

# Function to calculate pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000  # kPa

# Function to calculate Reynolds number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

# Function to calculate pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = 0.1 + (50 * reynolds_number) / (larger_diameter / smaller_diameter)**4 - 1
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000  # kPa

# Function to convert kPa to psi
def kpa_to_psi(pressure_kpa):
    return pressure_kpa * 0.1450377  # Conversion factor from kPa to psi

# Main function to calculate the pressure at the house
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    diameter = 0.28687  # PVC_SCHED80_INNER_DIAMETER
    friction = 0.013     # PVC_SCHED80_FRICTION_FACTOR
    velocity = 1.65      # SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, 0.048692)  # HDPE_SDR11_INNER_DIAMETER
    pressure += loss
    
    diameter = 0.048692  # HDPE_SDR11_INNER_DIAMETER
    friction = 0.018      # HDPE_SDR11_FRICTION_FACTOR
    velocity = 1.75       # HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    pressure_psi = kpa_to_psi(pressure)  # Convert to psi
    
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} psi")

if __name__ == "__main__":
    main()

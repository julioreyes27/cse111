# File: water_flow.py
# Author: Julio Reyes

# Summary: TODO 

# -Milestone version-

def main():
    # There are on indications for this program to be ran in the assignment page.
    pass

def water_column_height(tower_height, tank_height):
    
    water_column_height = tower_height + 3 * tank_height / 4
    return water_column_height

def pressure_gain_from_water_height(height):

    pressure = 998.2 * 9.80665 * height / 1000
    return pressure 

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
    pressure_loss = -friction_factor * pipe_length * 998.2 * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return pressure_loss

if __name__ == "__main__":
    main()

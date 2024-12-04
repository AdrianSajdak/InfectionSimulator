from simulation import Simulation

if __name__ == "__main__":
    scenario = 1 # SCENARIO 1 - NO IMMUNITY, 2 - 20% IMMUNITY
    simulation_area_width = 100
    simulation_area_height = 100
    initial_population = 50

    simulation = Simulation(simulation_area_width, simulation_area_height, initial_population, scenario)
    simulation.run()
    simulation.quit()

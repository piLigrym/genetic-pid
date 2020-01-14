import random
import math
import matplotlib.pyplot as plt
import os
from simulation import Simulation
import listtools
from config import config

if not os.path.exists(config['data_directory']):
    os.makedirs(config['data_directory'])

simulation = Simulation(config)

simulation.generate_initial_population()

#fitness_values = run_simulation(map, population)

max_values = []
avg_values = []
kp_values = []
kd_values = []
ki_values = []

# perform simulation

for i in range(config['max_runs']):

    simulation.generate_new_population()
    fitness_values = simulation.fitness_values
    population = simulation.population

    # add the champion chromosome to a list of champions for plotting
    index_of_champion = listtools.max_index_in_list(fitness_values)
    kp_values.append(population[index_of_champion].kp)
    kd_values.append(population[index_of_champion].kd)
    ki_values.append(population[index_of_champion].ki)


    # add the max/average values to lists for plotting
    max_values.append(listtools.max_value_in_list(fitness_values))
    avg_values.append(listtools.avgList(fitness_values))


    print("Run " + str(i) + ": max value " + str(max_values[i]) + ", avg value " + str(avg_values[i]))
    print(population[index_of_champion].kp, population[index_of_champion].kd, population[index_of_champion].ki)
    print('\n')

plt.figure()
plt.plot()
plt.title("Fitness Values Over Time")

plt.plot(range(config['max_runs']), max_values, label = r"Max Value")
plt.plot(range(config['max_runs']), avg_values, label = r"Average Value")
plt.legend(loc='lower right')
plt.xlabel("Run")
plt.ylabel("Value")
plt.savefig("fitness_values_over_time.png", format="png")

# plot values of parameters for each run
plt.figure()
plt.plot()
plt.title("Champion Gain Values Per Run")

plt.plot(range(config['max_runs']), kp_values, label = r"Kp")
plt.plot(range(config['max_runs']), kd_values, label = r"Kd")
plt.plot(range(config['max_runs']), ki_values, label = r"Ki")
plt.legend(loc='center right')
plt.xlabel("Run")
plt.ylabel("Value")
plt.savefig("champion_gain_values_per_run.png", format="png")


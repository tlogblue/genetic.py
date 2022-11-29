from operator import index
import random

# encoding
def generate_random_value (bound=100):
    return (random.random()*2-1)*bound
def creat_individual():
    return [generate_random_value() for _ in range(n)]

#compute fitness
def compute_fitness(individual):
    return 1/(0.00001 + sum (val*val for val in individual))

def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()
    for i in range (n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    
    return individual1_new, individual2_new

def mutate(individual, mutation_rate = 0.05):
    individual_m = individual.copy()
    
    for i in range (n):
        if random.random() < mutation_rate:
            individual_m[i] = generate_random_value()

    return individual_m
 
def selection (sorted_old_population):
    index1 = random.randint(0, m-1)
    index2 = random.randint(0, m-1)
    
    while index2 == index1:
        index2 = random.randint (0, m-1)
    
    individual_s = sorted_old_population [index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]
    return individual_s

n=6
m=100
n_generations = 300

#step1: step initial population
population = [creat_individual() for _ in range(m)]

#loops
elitism = 2
for i in range (n_generations):
    sorted_population = sorted (population, key = compute_fitness)
    
    #creat new_populations
    new_population = sorted_population[-elitism:]
    
    while len(new_population) < m:
        #selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)
        
        #crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)
        
        #mutation
        individual_m1 = mutate (individual_c1)
        individual_m2 = mutate (individual_c2)
        
        #copy
        new_population.append(individual_m1)
        new_population.append(individual_m2)
        
    #update
    population = new_population

import matplotlib.pyplot as plt    
plt.plot(fitnesses)
plt.show()

sorted_population = sorted(population, key = compute_fitness)
print (sorted_population[-1])




     

     
     
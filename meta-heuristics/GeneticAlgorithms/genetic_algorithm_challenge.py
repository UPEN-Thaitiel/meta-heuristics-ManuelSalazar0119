
# Genetic Algorithm - Step-by-Step Coding Challenge
# Objective: evolve a population to match the sequence [0, 1, 2, ..., 9]

# STEP 1: Define constants
# - SOLUTION_SEQUENCE: target sequence from 0 to 9
# - TOURNAMENT_SIZE: size of the population used in tournament selection
# - MAX_FITNESS: value indicating perfect match
# - CHROMOSOME_LENGTH: number of genes per individual

# STEP 2: Define the Individual class
# - Constructor: initialize a chromosome of CHROMOSOME_LENGTH with random integers
# - get_fitness(): return the number of positions where gene matches the SOLUTION_SEQUENCE
# - set_gene(index, value): modify gene at specific index
# - __repr__: for readable printing of chromosomes

# STEP 3: Define the Population class
# - Constructor: generate a list of Individuals of given size
# - get_fittest(): return individual with highest fitness
# - get_fittest_elitism(n): return top-n individuals sorted by fitness
# - get_size(): return the population size
# - get_individual(index): return individual at given index
# - save_individual(index, individual): replace individual at index

# STEP 4: Define the GeneticAlgorithm class
# - Constructor: set population size, crossover rate, mutation rate, elitism size

# STEP 5: Implement the run method
# - Create initial population
# - Loop until max fitness is found:
#     - Print current generation number and fittest individual
#     - Evolve population using evolve_population()

# STEP 6: evolve_population()
# - Create new Population
# - Apply elitism: copy top 'elitism_param' individuals from old population
# - For remaining slots:
#     - Select two parents using random_selection()
#     - Apply crossover and add result to new population
# - Apply mutation on all individuals in new population
# - Return new population

# STEP 7: crossover(offspring1, offspring2)
# - Choose random crossover points start and end
# - Create new individual with:
#     - genes from parent 1 before 'start'
#     - genes from parent 2 between 'start' and 'end'
#     - genes from parent 1 after 'end'

# STEP 8: mutate(individual)
# - For each gene, with probability = mutation_rate:
#     - Replace gene with new random integer in range [0, CHROMOSOME_LENGTH)

# STEP 9: random_selection(actual_population)
# - Create temporary population of TOURNAMENT_SIZE
# - Fill with individuals randomly selected from actual population
# - Return the fittest from this mini-tournament

# STEP 10: Main execution
# - Instantiate GeneticAlgorithm and call run()

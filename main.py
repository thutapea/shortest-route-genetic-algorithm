import random
import math

# Constants
ROWS = 4
COLUMNS = 42
SHELVES = ROWS * COLUMNS
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.9
POPULATION_SIZE = 24
GENERATIONS = 1000

shelves = []
for i in range(ROWS):
    for j in range(COLUMNS):
        shelves.append((i, j))  # add tuple pair to list to populate graph


def m_distance(p1, p2):  # distance function
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
# chose manhattan distance function as it's
#   inexpensive, simple, models purely grid-like movement between bookshelves


# Cost calculation
def t_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += m_distance(route[i], route[i + 1])
    distance += m_distance(route[-1], route[0])  # remember closure
    return distance


# Optimizing route == decreasing distance == increasing reciprocal distance
def fitness(route):
    return 1 / t_distance(route)



def populate(size):
    population = []
    for _ in range(size):
        route = random.sample(shelves, SHELVES)  # Assign a random 24 shelve locations
        population.append(route)
    return population
# Choose  parents
def select_parents(population):
    tournament_size = 5 # can be 7, 8, or 9 even as convergence did not seem to be an issue
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: t_distance(x))  # cool code optimization using lambda function
    return tournament[0], tournament[1]


# genetic algorithm function.
# Here, ill choose a crossover point to pass on, then fill in the rest with the other parents genes
def order_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(SHELVES), 2))
    child = [-1] * SHELVES #can't be 0, as segment may be0...
    child[start:end + 1] = parent1[start:end + 1]

    idx = 0
    for i in range(SHELVES):
        if parent2[i] not in child:
            while child[idx] != -1:
                idx += 1
            child[idx] = parent2[i]

    return child


# Uses mutation rate to randomly swap shelves
def mutate(route):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(SHELVES), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]


# Main Genetic Algorithm
def genetic_algorithm():

    population = populate(POPULATION_SIZE)

    for generation in range(GENERATIONS):
        population.sort(key=lambda x: t_distance(x))  # Sort

        best_route = population[0]  # save best route
        best_distance = t_distance(best_route)

        next_generation = population[:10]  # only best 10% survive

        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population)

            if random.random() < CROSSOVER_RATE:
                child = order_crossover(parent1, parent2)
            else:
                child = parent1[:]

            mutate(child)

            next_generation.append(child)

        population = next_generation

        if generation % 100 == 0:
            print(f"Generation {generation}, Best Distance: {best_distance}")

    return best_route, best_distance


# Main function
def main():
    best_route, best_distance = genetic_algorithm()
    print("\nOptimized Route:")
    print(best_route)
    print("Total Distance: ", best_distance)


if __name__ == "__main__":
    main()
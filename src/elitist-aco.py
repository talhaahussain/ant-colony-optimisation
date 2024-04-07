import load_data
import ant
import matplotlib.pyplot as plt
from statistics import mean
import time


def evaporate_pheromones(T, rate = 0.5):
    """
    Function for evaporating pheromones.

    Args:
        T ([[int]]): A pheromone matrix for evaporation
        rate (int): The rate at which evaporation should take place from all cells
    """
    for i in range(len(T)):
        for j in range(len(T)):
            # Evaporates off a certain proportion of pheromone from every cell
            T[i][j] = (1-rate) * T[i][j]


def setup(num_ants, filename):
    """
    Function for setting up ACO program.

    Args:
        num_ants (int): Number of ants per colony/generation
        filename (String): Name of XML file to be opened

    Returns:
        d ([[int]]): Distance matrix of cities extracted from XML file
        H ([[int]]): Generated heuristic matrix (default)
        T ([[int]]): Generated pheromone matrix (default)
        ants ([Ant]): A list of all ant object instantiated
    """
    # Load XML data into distance matrix
    d = load_data.get_distance_matrix(filename)
    
    # Generate default heuristic and pheromone matrices
    H = [[round(1/d[i][j], 4) if i != j else 0 for j in range(len(d))] for i in range(len(d))]
    T = [[1 for j in range(len(d))] for i in range(len(d))]

    ants = []

    for i in range(num_ants):
        # Populate list with Ant objects; assign them all IDs
        ants.append(ant.Ant(i))

    return d, H, T, ants


def main(ant_count, evaporation_rate, max_iterations, dataset):
    """
    Main method. Run on start-up.
    """

    start = time.time() # For time-keeping purposes
    d, H, T, ants = setup(ant_count, dataset)
    
    t = max_iterations # Number of max iterations

    # The following four lists are used for statistics tracking and logging
    distances = []
    averages = []
    best_in_gen = []
    worst_in_gen = []
    
    for x in range(t):
        print("ITERATION: " + str(x) + "\n")
        for a in ants:
            for city in range(len(d) - 1):
                a.visit_city(d, H, T)
            a.visited.append(a.start) # Appends start city to the end of the route, closing it
            dist = a.calculate_distance(d)
            print("Ant " + str(a.ant_id) + " route: " + str(a.visited))
            print("Distance: " + str(dist) + "\n")
            a.best_solution(x) # Check if this solution is the best one yet
            distances.append(dist)
        
        # The following computes statistics for this iteration
        best_in_gen.append(min(distances))
        worst_in_gen.append(max(distances))
        averages.append(mean(distances))

        evaporate_pheromones(T, evaporation_rate)
        flag = True
        for a in ants:
            if a.best_distance == best_in_gen[-1] and flag == True:
                a.deposit_best_pheromone(T)
                flag = False # To ensure pheromone isn't repeatedly dumped

            a.deposit_pheromone(T)
            a.clear_visited()
        
        distances.clear() # Resets list to be used in next iteration
        print("\n")
    
    end = time.time()

    duration = end - start

    print("Duration is: " + str(duration) + " seconds.")

    # The following are all for graphing purposes
    plt.title("Ant Colony Optimisation")
    plt.xlabel("Iterations")
    plt.ylabel("Distance")
    plt.plot(range(t), best_in_gen, label = "Best distances")
    plt.plot(range(t), worst_in_gen, label = "Worst distances")
    plt.plot(range(t), averages, label = "Average distances")
    plt.legend()
    plt.show()



        
    for a in ants:
        print("Ant " + str(a.ant_id) + " best iteration: " + str(a.best_iteration))
        print("Best route: " + str(a.best_path))
        print("Best distance: " + str(a.best_distance) + "\n")

if __name__ == "__main__":
    # Run main() iff file isn't imported
    main(4, 0.5, 100, "brazil58.xml") # MODIFY PARAMETERS HERE!

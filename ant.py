import random

class Ant:
    """
    Ant class for Ant Colony Optimization.

    Attributes:
        ant_id (int): ID number for ant object
        visited ([int]): List of visited locations
        distance (int): Distance travelled between cities in total
        start (int): Starting location (city) of ant
        best_distance (int): Minimum distance found by this ant over its lifetime
        best_path ([int]): Best path found by this ant over its lifetime
        best_iteration (int): Iteration in which best distance/path was found by this ant

    Methods:
        __init__(self, ant_id, start)
        calculate_distance(self, cities)
        visit_city(self, d, H, T, alpha, beta)
        deposit_pheromone(self, T)
        clear_visited(self)
        best_solution(self, iteration)

    """
    def __init__(self, ant_id, start=0):
        """
        Constructor for Ant class.
        """
        self.ant_id = ant_id
        self.visited = [start]
        self.distance = 0
        self.start = start
        self.best_distance = 0
        self.best_path = []
        self.best_iteration = 0

    def calculate_distance(self, cities):
        """
        Method for finding the distance traversed across a list of cities.
        
        Args:
            cities ([[int]]): A distance matrix for the selected cities

        Returns:
            dist (int): Distance covered in path for this ant across selected cities
        """
        dist = 0
        for i in range(len(self.visited)):
            if self.visited[i] == self.visited[0] and i != 0:
            # If arrived back  at first city, break out of loop
                break
            else:
            # Continue to measure distance, extracting values from distance matrix
                dist += cities[self.visited[i]][self.visited[i + 1]]                    
        self.distance = dist
        return dist

    def visit_city(self, d, H, T, alpha=1, beta=2):
        """
        Method for randomly visiting a new city. Looped continuously in main() to generate a new path.

        Args:
            d ([[int]]): A distance matrix for the selected cities
            H ([[int]]): A heuristic matrix for the selected cities
            T ([[int]]): A pheromone matrix for the selected cities
            alpha (int): A variable for the significance of pheromones when selecting next city
            beta (int): A variable for the significance of heuristic when selecting next city
        """
        cities = len(d)
        for i in range(cities):
            for j in range(cities):
                if i != j and j not in self.visited:
                # City may only be visited iff it has not already been visited
                    H[i][j] = round(1/d[i][j], 4)
                else:
                    H[i][j] = 0

        N = [None] * cities
        i = self.visited[-1]
        den = 0
        for j in range(cities):
            # Apply modifier pheromone and heuristic matrices
            N[j] = T[i][j] **alpha * H[i][j] **beta
            den += N[j]
        
        P = [None] * cities
        for j in range(cities):
            P[j] = N[j] / den

        rand = random.random()
        CP = 0
        for i in range(cities):
            # Randomly select a city
            CP += P[i]
            if CP >= rand:
                # Add city to visited cities
                self.visited.append(i)
                break
        
    def deposit_pheromone(self, T):
        """
        Method for depositing ant pheromone into pheromone matrix T.

        Args:
            T ([[int]]): Matrix in which to deposit pheromone
        """
        delta = 1/self.distance
        for i in range(len(T)):
            # Deposit pheromone in visited locations, based on distance covered
            T[self.visited[i]][self.visited[i+1]] += delta

    def deposit_best_pheromone(self, T):
        """
        Method for depositing best ant pheromone into pheromone matrix T.

        Args:
            T ([[int]]): Matrix in which to deposit pheromone
        """

        delta = 1/self.best_distance
        for i in range(len(T)):
            # Deposite pheromone in visited locations, based on distance covered
            T[self.best_path[i]][self.best_path[i+1]] += delta

    def clear_visited(self):
        """
        Method for clearing all visited cities and resetting distance.
        """
        self.visited = [0]
        self.distance = 0

    def best_solution(self, iteration):
        """
        Method for recording best ant performance.
        
        Args:
            iteration (int): Iteration in which metrics occurred

        Returns:
            Boolean: True if this iteration is the best performance thusfar;
                     False otherwise.
        """
        if self.distance < self.best_distance or self.best_distance == 0:
            # If this solution is the best, update all metrics to this new record
            self.best_distance = self.distance
            self.best_path = self.visited
            self.best_iteration = iteration
            return True
        return False

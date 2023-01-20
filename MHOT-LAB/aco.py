#initialize parameters

### Ants : no of ants 10
Ants = 50
### Alpha : controls the importance of the pheromone trail in the decision-making process of the ants.
A = 1.0
### Beta: controls the importance of the heuristic information (distance, visibility, etc.) in the decision-making process of the ants.
B = 2.0
### Rho: controls the pheromone evaporation rate.
rho = 0.05
### Q: controls the amount of pheromone deposited by the ants.
Q = 1.0
### Tau0: initial pheromone trail level.
tau0 = 0.5
### Iterations i: number of times the algorithm will run.
i = 20
### Initialization "initiate": method for initializing the pheromone trails.
initiate = "random "
### Local Search "Ls" : method used to improve the solution constructed by the ants.
LS = "2-opt"
### Pheromone update "P_update" : method used to update the pheromone trails.
P_update = "global_update "
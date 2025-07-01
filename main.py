import numpy as np
from path_planner import find_path

grid = np.zeros((100, 100), dtype=int)
np.random.seed(0)
obstacle_indices = np.random.choice(100*100, size=2000, replace=False)
grid[np.unravel_index(obstacle_indices, grid.shape)] = 1

start = (0, 0)
goal = (99, 99)

path = find_path(start, goal, grid)
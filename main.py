import numpy as np
import math
from path_planner import find_path
from diff_drive import differential_drive_astar

grid = np.zeros((100, 100), dtype=int)
np.random.seed(0)
obstacles = np.random.choice(100*100, size=2000, replace=False)
grid[np.unravel_index(obstacles, grid.shape)] = 1

start = (0, 0)
goal = (99, 99)

print("=== Milestone 1: Grid-based A* ===")
path1 = find_path(start, goal, grid)
if path1:
    print(f"Path length: {len(path1)} steps")
else:
    print("No path found.")

print("\n=== Milestone 2: Differential Drive A* ===")
path2 = differential_drive_astar(start, goal, grid)
if path2:
    print(f"Path length: {len(path2)} poses")
    for x, y, theta in path2[:5]:
        print(f"x={x:.2f}, y={y:.2f}, θ={math.degrees(theta):.1f}°")
else:
    print("No path found.")

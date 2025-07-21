import numpy as np
import matplotlib.pyplot as plt
from path_planner import find_path

# Load occupancy grid and relative trajectory
grid = np.load("occupancy_grid.npy")
traj = np.load("relative_trajectory.npy")

GRID_RES = 0.1
MAP_ORIGIN = np.array([grid.shape[0] // 2, grid.shape[1] // 2])

# Pick a sample segment (you can loop over others too)
i = 100
start_pos = traj[i]
goal_pos = traj[i + 50]

# Convert to grid indices
def to_grid_coords(pos):
    return np.floor(pos / GRID_RES).astype(int) + MAP_ORIGIN

start_cell = tuple(to_grid_coords(start_pos))
goal_cell = tuple(to_grid_coords(goal_pos))

# Run A* planner
path = find_path(start_cell, goal_cell, grid)

# Extract actual segment of trajectory
actual_segment = traj[i:i+51]

# Plot both
plt.figure(figsize=(10, 10))
plt.imshow(grid, cmap='gray_r', origin='lower')
plt.title("Milestone 3C: Planned vs Actual Trajectory")

# Plot planned path
if path:
    xs = [p[1] for p in path]
    ys = [p[0] for p in path]
    plt.plot(xs, ys, color='blue', label='Planned A* Path')

# Plot actual trajectory
actual_xs = [to_grid_coords(p)[1] for p in actual_segment]
actual_ys = [to_grid_coords(p)[0] for p in actual_segment]
plt.plot(actual_xs, actual_ys, color='orange', label='Actual Robot Path')

plt.scatter(start_cell[1], start_cell[0], color='green', label='Start')
plt.scatter(goal_cell[1], goal_cell[0], color='red', label='Goal')
plt.legend()
plt.grid(True)
plt.show()

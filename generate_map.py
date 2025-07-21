import os
import numpy as np
import pickle

# Load traj_data
with open("traj_data.pkl", "rb") as f:
    odom = pickle.load(f)

# Map parameters
GRID_RES = 0.1  # meters per cell
MAP_SIZE = 1000  # 1000x1000 grid
ROBOT_HEIGHT = 0.4
map_origin = np.array([MAP_SIZE // 2, MAP_SIZE // 2])  # place origin in center
occ_grid = np.zeros((MAP_SIZE, MAP_SIZE), dtype=np.uint8)

# Path to point clouds
pcd_dir = "pcd"

for i in range(len(odom["position"])):
    # Load point cloud
    cloud = np.load(os.path.join(pcd_dir, f"{i}.npz"))["arr_0"]

    # Filter out ground points
    cloud = cloud[cloud[:, 2] > ROBOT_HEIGHT]

    # Transform to global frame
    pos = np.array(odom["position"][i])
    yaw = odom["yaw"][i]
    R = np.array([[np.cos(yaw), -np.sin(yaw)], [np.sin(yaw), np.cos(yaw)]])
    points_global = (R @ cloud[:, :2].T).T + pos[:2]

    # Convert to grid indices
    indices = np.floor(points_global / GRID_RES).astype(int)
    indices += map_origin  # shift origin to center of grid

    # Filter indices inside map
    mask = (indices[:, 0] >= 0) & (indices[:, 0] < MAP_SIZE) & \
           (indices[:, 1] >= 0) & (indices[:, 1] < MAP_SIZE)
    indices = indices[mask]

    # Mark as occupied
    occ_grid[indices[:, 1], indices[:, 0]] = 1  # y,x for image-style plotting

# Save the final map
np.save("occupancy_grid.npy", occ_grid)
print("Occupancy grid saved to occupancy_grid.npy")

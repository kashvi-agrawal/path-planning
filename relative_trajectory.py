import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("traj_data.pkl", "rb") as f:
    odom = pickle.load(f)

positions = np.array(odom["position"])
yaws = np.array(odom["yaw"])

# Set the first pose as origin
origin_pos = positions[0]
origin_yaw = yaws[0]

def transform_to_relative(p, yaw):
    """Rotate and translate point p to be relative to origin."""
    # Shift
    shifted = p - origin_pos
    # Rotate
    c, s = np.cos(-origin_yaw), np.sin(-origin_yaw)
    R = np.array([[c, -s], [s, c]])
    return R @ shifted[:2]  # Only x, y

# Compute relative trajectory
relative_traj = [transform_to_relative(p, y) for p, y in zip(positions, yaws)]
relative_traj = np.array(relative_traj)

# Save for reuse later
np.save("relative_trajectory.npy", relative_traj)

# Plot
plt.figure(figsize=(8, 8))
plt.plot(relative_traj[:, 0], relative_traj[:, 1], label="Relative Trajectory")
plt.scatter(0, 0, color='green', label='Start')
plt.title("Milestone 3B: Robot's Relative Trajectory")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

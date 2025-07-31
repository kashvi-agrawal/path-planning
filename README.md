**Robot Navigation – Path Planning and Occupancy Grid Mapping**

This repository contains my implementation of robot path planning modules across three milestones. The project builds from basic grid-based planning to realistic differential-drive motion planning and finally generates an occupancy grid from real 3D LiDAR sensor data. The final milestone compares the robot’s actual driven path with what a grid-based planner would have suggested in the same environment.

**Overview** 

  🔹 Milestone 1: Planning in an Occupancy Grid
      - Implements a standard A* search algorithm to find a feasible path on a binary 2D occupancy grid.
      - Environment: 100×100 grid with randomly placed obstacles.
      - Output: A valid path from start to goal.
  🔹 Milestone 2: Including a Robot Model
      - Extends planning to a differential drive robot, accounting for motion constraints and heading.
      - Introduces wheel velocities and motion primitives.
      - Produces a realistic, smooth path reflecting nonholonomic robot movement.
  🔹 Milestone 3: Real Sensor Data Integration
      - 3A – Occupancy Grid Generation:
          - Processes 379 LiDAR point cloud scans and odometry data.
          - Filters ground points, transforms each scan into a global frame, and builds a 2D occupancy grid.
      - 3B – Relative Trajectory:
          - Computes the robot’s trajectory relative to its starting pose.
      - 3C – Planned vs Actual Path:
          - Runs A* path planning on the real occupancy grid.
          - Compares the computed path to the robot’s actual driven trajectory.

**Project Structure**
.
├── main.py                    # Milestones 1 & 2: Grid-based and Differential Drive A*
├── path_planner.py            # A* algorithm implementation
├── diff_drive.py              # Differential drive motion planner
├── visualisation.py           # Visualization utilities
│
├── generate_map.py            # Milestone 3A: Generate occupancy grid from LiDAR
├── relative_trajectory.py     # Milestone 3B: Compute relative trajectory
├── compare_path.py            # Milestone 3C: Compare planned vs actual trajectory
│
├── traj_data.pkl              # Odometry data (provided)
├── pcd                        # Folder containing 379 LiDAR `.npz` files
├── occupancy_grid.npy         # Generated map (output of 3A)
└── relative_trajectory.npy    # Relative trajectory (output of 3B)

**How to Run**

1) Milestones 1 & 2 → python main.py
2) Milestone 3A → python generate_map.py
3) Milestone 3B → python relative_trajectory.py
4) Milestone 3C → python compare_path.py

**Visualization**

visualisation.py plots occupancy grids and planned paths.
compare_path.py shows an overlay of:
  - 🟦 Planned Path (A*)
  - 🟧 Actual Robot Trajectory
  - 🟩 Start and 🟥 Goal positions

**Requirements**
  - Python 3.x
  - NumPy
  - Matplotlib





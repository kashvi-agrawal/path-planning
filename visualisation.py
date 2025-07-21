import numpy as np
import matplotlib.pyplot as plt

def plot_grid_path(grid, path=None, title="Occupancy Grid", is_diff_drive=False):
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='gray_r', origin='lower')

    if path:
        if is_diff_drive:
            xs = [p[0] for p in path]
            ys = [p[1] for p in path]
        else:
            xs = [p[1] for p in path]
            ys = [p[0] for p in path]
        plt.plot(xs, ys, color='blue', linewidth=2, label='Path')
        plt.scatter(xs[0], ys[0], color='green', label='Start')
        plt.scatter(xs[-1], ys[-1], color='red', label='Goal')

    plt.title(title)
    plt.xlabel("X (grid index)")
    plt.ylabel("Y (grid index)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    grid = np.load("occupancy_grid.npy")  # From Milestone 3A
    plot_grid_path(grid, title="Milestone 3A: Occupancy Grid from 3D LiDAR")

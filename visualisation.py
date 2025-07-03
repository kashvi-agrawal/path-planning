import matplotlib.pyplot as plt

def plot_grid_path(grid, path, title, is_diff_drive=False):
    plt.figure(figsize=(8, 8))
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
    plt.legend()
    plt.grid(True)
    plt.show()

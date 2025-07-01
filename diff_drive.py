import math
import heapq

def simulate_differential_drive(x, y, theta, vl, vr, dt, wheelbase):
    v = (vr + vl) / 2.0
    omega = (vr - vl) / wheelbase
    if abs(omega) < 1e-6:
        x_new = x + v * math.cos(theta) * dt
        y_new = y + v * math.sin(theta) * dt
        theta_new = theta
    else:
        R = v / omega
        cx = x - R * math.sin(theta)
        cy = y + R * math.cos(theta)
        theta_new = theta + omega * dt
        x_new = cx + R * math.sin(theta_new)
        y_new = cy - R * math.cos(theta_new)
    return x_new, y_new, theta_new

def differential_drive_astar(start, goal, grid, wheelbase=0.5, dt=0.1):
    rows, cols = grid.shape
    visited = set()
    came_from = {}
    cost_so_far = {}

    def heuristic(x, y):
        return math.hypot(goal[0] - x, goal[1] - y)

    def discretize(state, resolution=0.1, angle_bins=24):
        x, y, theta = state
        return (round(x / resolution), round(y / resolution), round(theta * angle_bins / (2 * math.pi)) % angle_bins)

    start_state = (*start, 0.0)
    goal_pos = goal
    cost_so_far[discretize(start_state)] = 0
    came_from[discretize(start_state)] = None
    frontier = [(heuristic(*start), 0, start_state)]

    motion_primitives = [
        (1.0, 1.0), (0.5, 1.0), (1.0, 0.5),
        (0.0, 1.0), (1.0, 0.0), (-1.0, 1.0), (1.0, -1.0)
    ]

    while frontier:
        _, g, current = heapq.heappop(frontier)
        x, y, theta = current
        key = discretize(current)

        if key in visited:
            continue
        visited.add(key)

        if int(round(x)) == goal_pos[0] and int(round(y)) == goal_pos[1]:
            path = [current]
            while came_from[key] is not None:
                key = came_from[key]
                state = (key[0] * 0.1, key[1] * 0.1, key[2] * (2 * math.pi) / 24)
                path.append(state)
            return path[::-1]

        for vl, vr in motion_primitives:
            x_new, y_new, theta_new = simulate_differential_drive(x, y, theta, vl, vr, dt, wheelbase)
            if 0 <= int(x_new) < cols and 0 <= int(y_new) < rows and grid[int(y_new)][int(x_new)] == 0:
                new_state = (x_new, y_new, theta_new)
                new_key = discretize(new_state)
                step_cost = math.hypot(x_new - x, y_new - y)
                g_new = g + step_cost
                if new_key not in cost_so_far or g_new < cost_so_far[new_key]:
                    cost_so_far[new_key] = g_new
                    f = g_new + heuristic(x_new, y_new)
                    heapq.heappush(frontier, (f, g_new, new_state))
                    came_from[new_key] = key
    return None

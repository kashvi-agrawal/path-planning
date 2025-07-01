import heapq
import math

def find_path(start, goal, grid):
    rows, cols = grid.shape
    visited = set()
    came_from = {}
    cost_so_far = {}

    def heuristic(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), 0, start))
    came_from[start] = (None, 0)
    cost_so_far[start] = 0

    while frontier:
        _, cost_current, current = heapq.heappop(frontier)

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current][0]
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            x, y = neighbor
            if 0 <= x < rows and 0 <= y < cols:
                if grid[x][y] == 0:
                    step_cost = math.hypot(dx, dy)
                    g_new = cost_so_far[current] + step_cost
                    if neighbor not in cost_so_far or g_new < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = g_new
                        f_new = g_new + heuristic(neighbor, goal)
                        heapq.heappush(frontier, (f_new, g_new, neighbor))
                        came_from[neighbor] = (current, g_new)

    return None
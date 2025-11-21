# bfs_an.py
# BFS implementation for shortest path in classmate graph
# Author: An

from collections import deque
import graph_module  # file: graph_data.py, biến: GRAPHX

def BFS_An(graph_dict, start, goal):
    if start not in graph_dict:
        return None, [], f"Error: Start student '{start}' does not exist."
    if goal not in graph_dict:
        return None, [], f"Error: Goal student '{goal}' does not exist."

    queue = deque([(start, [start])])
    visited = {start}              # mark visited on enqueue
    expanded = []

    while queue:
        current, path = queue.popleft()
        expanded.append(current)

        if current == goal:
            return path, expanded, None

        for nb in sorted(graph_dict[current]):   # sort for stable output
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, path + [nb]))

    return None, expanded, f"Sorry, no connection between '{start}' and '{goal}'."

if __name__ == "__main__":
    graph = graph_module.GRAPHX

    print("=== Dolly needs introduction to Bat An ===")
    path, expanded, err = BFS_An(graph, "Dolly", "Bat An")
    if path:
        print("Shortest path:", " -> ".join(path))
    else:
        print(err)
    print("Traversed (expanded order):", ", ".join(expanded))

    print("\n=== George needs introduction to Bob ===")
    path, expanded, err = BFS_An(graph, "George", "Bob")
    if path:
        print("Shortest path:", " -> ".join(path))
    else:
        print(err)
    print("Traversed (expanded order):", ", ".join(expanded))

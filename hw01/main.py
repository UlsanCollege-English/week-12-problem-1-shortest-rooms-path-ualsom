"""
HW01 — Shortest Rooms Path (BFS)
"""

from collections import deque

def bfs_shortest_path(graph, start, goal):
    """Return shortest path from start to goal using BFS.
    Return empty list if no path or start/goal not in graph.
    """
    if start not in graph or goal not in graph:
        return []

    if start == goal:
        return [start]

    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
                if neighbor == goal:
                    # reconstruct path
                    path = [goal]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path

    return []  # goal not reachable

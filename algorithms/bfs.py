from collections import deque

def bfs(graph, start_id, end_id):
    queue = deque([start_id])
    came_from = {node: None for node in graph.nodes}
    visited_order = []

    while queue:
        current_node = queue.popleft()
        visited_order.append(current_node)

        if current_node == end_id:
            # Reconstruct path
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            return path, visited_order

        for edge in graph.nodes[current_node].edges:
            neighbor = edge.node2.id if edge.node1.id == current_node else edge.node1.id
            if came_from[neighbor] is None and neighbor != start_id:  # Not visited
                came_from[neighbor] = current_node
                queue.append(neighbor)

    return None, visited_order  # No path found

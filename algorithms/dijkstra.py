from heapq import heappush, heappop

def dijkstra(graph, start_id, end_id):
    # Priority queue for nodes to explore
    pq = [(0, start_id)]  # (distance, node_id)
    distances = {node_id: float('inf') for node_id in graph.nodes}  # Use node_id as key
    distances[start_id] = 0
    came_from = {node_id: None for node_id in graph.nodes}  # Tracks the path
    visited_order = []  # Order in which nodes are finalized (popped)

    while pq:
        current_distance, current_node = heappop(pq)

        # Skip if this is an outdated queue entry
        if current_distance > distances[current_node]:
            continue

        visited_order.append(current_node)

        # Early exit if we've reached the target node
        if current_node == end_id:
            break

        # Explore neighbors
        for edge in graph.nodes[current_node].edges:
            # Determine the neighbor node ID
            neighbor = edge.node2.id if edge.node1.id == current_node else edge.node1.id
            new_distance = current_distance + edge.weight

            # If a shorter path is found, update distances and the path
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                came_from[neighbor] = current_node
                heappush(pq, (new_distance, neighbor))

    # Reconstruct the shortest path
    path = []
    current = end_id
    while current is not None:
        path.insert(0, current)
        current = came_from[current]
    return path, visited_order

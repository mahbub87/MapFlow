from heapq import heappop, heappush
import math

def a_star(graph, start_id, end_id):
    # Priority queue for the open list
    open_list = []
    open_set = set()  # Tracks nodes currently in the open list
    closed_set = set()  # Tracks nodes already processed

    # Dictionaries to track costs and path reconstruction
    came_from = {node: None for node in graph.nodes}
    g_score = {node: float('inf') for node in graph.nodes}
    f_score = {node: float('inf') for node in graph.nodes}

    # Initialize the start node
    g_score[start_id] = 0
    f_score[start_id] = heuristic(graph, start_id, end_id)
    heappush(open_list, (f_score[start_id], start_id))
    open_set.add(start_id)

    while open_list:
        # Pop the node with the lowest f_score
        _, current_node = heappop(open_list)
        open_set.remove(current_node)

        if current_node == end_id:
            # Reconstruct and return the path
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            return path

        # Mark the current node as processed
        closed_set.add(current_node)

        # Explore neighbors
        for edge in graph.nodes[current_node].edges:
            neighbor = edge.node2.id if edge.node1.id == current_node else edge.node1.id

            if neighbor in closed_set:
                continue  # Skip already processed nodes

            tentative_g_score = g_score[current_node] + edge.weight

            if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                # Update path and costs for this neighbor
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(graph, neighbor, end_id)

                if neighbor not in open_set:
                    heappush(open_list, (f_score[neighbor], neighbor))
                    open_set.add(neighbor)

    return None  # No path found

def heuristic(graph, node_id, end_id):
    # Heuristic: straight-line distance between nodes
    node = graph.nodes[node_id]
    end_node = graph.nodes[end_id]
    return math.hypot(node.latitude - end_node.latitude, node.longitude - end_node.longitude)

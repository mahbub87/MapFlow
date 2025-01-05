def bidirectional_search(graph, start_id, end_id):
    front_queue = {start_id}
    back_queue = {end_id}
    front_came_from = {start_id: None}
    back_came_from = {end_id: None}

    while front_queue and back_queue:
        # Expand front
        next_front = set()
        for node in front_queue:
            for edge in graph.nodes[node].edges:
                neighbor = edge.node2.id if edge.node1.id == node else edge.node1.id
                if neighbor not in front_came_from:
                    front_came_from[neighbor] = node
                    next_front.add(neighbor)

        front_queue = next_front

        # Expand back
        next_back = set()
        for node in back_queue:
            for edge in graph.nodes[node].edges:
                neighbor = edge.node2.id if edge.node1.id == node else edge.node1.id
                if neighbor not in back_came_from:
                    back_came_from[neighbor] = node
                    next_back.add(neighbor)

        back_queue = next_back

        # Check for intersection
        intersection = front_queue.intersection(back_queue)
        if intersection:
            path = []
            meeting_point = intersection.pop()

            # Reconstruct forward path
            current = meeting_point
            while current is not None:
                path.insert(0, current)
                current = front_came_from[current]

            # Reconstruct backward path
            current = back_came_from[meeting_point]
            while current is not None:
                path.append(current)
                current = back_came_from[current]

            return path

    return None  # No path found

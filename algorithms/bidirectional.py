from collections import deque

def bidirectional_search(graph, start_id, end_id):
    if start_id == end_id:
        return [start_id], [start_id]

    # Queues for BFS from both ends
    front_q = deque([start_id])
    back_q = deque([end_id])

    # Visited sets and parent maps
    front_visited = {start_id}
    back_visited = {end_id}
    front_came_from = {start_id: None}
    back_came_from = {end_id: None}

    visited_order = []

    def reconstruct(meeting):
        path = []
        # forward part: start -> meeting
        cur = meeting
        while cur is not None:
            path.insert(0, cur)
            cur = front_came_from[cur]
        # backward part: from node after meeting to end
        cur = back_came_from[meeting]
        while cur is not None:
            path.append(cur)
            cur = back_came_from[cur]
        return path

    while front_q and back_q:
        # Expand the smaller frontier to keep work balanced
        if len(front_q) <= len(back_q):
            level_size = len(front_q)
            for _ in range(level_size):
                node = front_q.popleft()
                visited_order.append(node)
                for edge in graph.nodes[node].edges:
                    neighbor = edge.node2.id if edge.node1.id == node else edge.node1.id
                    if neighbor in front_visited:
                        continue
                    front_visited.add(neighbor)
                    front_came_from[neighbor] = node
                    if neighbor in back_visited:
                        return reconstruct(neighbor), visited_order
                    front_q.append(neighbor)
        else:
            level_size = len(back_q)
            for _ in range(level_size):
                node = back_q.popleft()
                visited_order.append(node)
                for edge in graph.nodes[node].edges:
                    neighbor = edge.node2.id if edge.node1.id == node else edge.node1.id
                    if neighbor in back_visited:
                        continue
                    back_visited.add(neighbor)
                    back_came_from[neighbor] = node
                    if neighbor in front_visited:
                        return reconstruct(neighbor), visited_order
                    back_q.append(neighbor)

    return None, visited_order  # No path found

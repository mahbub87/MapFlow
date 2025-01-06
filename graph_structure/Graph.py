import json

from graph_structure.Edge import Edge
from graph_structure.Node import Node


class Graph:

    def __init__(self):
        self.start_node = None
        self.nodes = {}

    def get_node(self, id):
        return self.nodes.get(id)

    def add_node(self, id, latitude, longitude):
        node = Node(id, latitude, longitude)
        self.nodes[node.id] = node
        return node

    def to_dict(self):
        return {
            'start_node_id': self.start_node.id if self.start_node else None,
            'nodes': {node_id: node.to_dict() for node_id, node in self.nodes.items()}
        }

    def from_dict(self, data):
        node_dict = {node_data['id']: Node.from_dict(node_data) for node_data in data['nodes'].values()}

        for node_data in data['nodes'].values():
            node = node_dict[node_data['id']]
            for edge_data in node_data['edges']:
                node1 = node_dict[edge_data['node1_id']]
                node2 = node_dict[edge_data['node2_id']]
                if not any(e.node1 == node1 and e.node2 == node2 for e in node1.edges):
                    edge = Edge(node1, node2)
                    edge.visited = edge_data['visited']
                    node1.edges.append(edge)
                    node2.edges.append(edge)

        self.nodes = node_dict
        self.start_node = node_dict.get(data['start_node_id'])

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        graph = cls()
        graph.from_dict(data)
        return graph

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            graph = cls()
            graph.from_dict(data)
            return graph

    def reset_shortest_path(self):
        for node in self.nodes.values():
            for edge in node.edges:
                edge.shortestPath = False

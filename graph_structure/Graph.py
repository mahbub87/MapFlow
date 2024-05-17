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
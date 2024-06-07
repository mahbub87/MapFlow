from math import hypot


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.visited = False

    def get_other_node(self, node):
        return self.node2 if node == self.node1 else self.node1

    @property
    def weight(self):
        return hypot(self.node1.latitude - self.node2.latitude, self.node1.longitude - self.node2.longitude)

    def to_dict(self):
        return {
            'node1_id': self.node1.id,
            'node2_id': self.node2.id,
            'visited': self.visited
        }
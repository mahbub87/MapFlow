from graph_structure.Edge import Edge

class Node:

    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.edges = []
        self.reset()

    @property
    def total_distance(self):
        return self.distance_from_start + self.distance_to_end

    @property
    def neighbors(self):
        return [{'node': edge.get_other_node(self), 'edge': edge} for edge in self.edges]

    def connect_to(self, node):
        edge = Edge(self, node)
        self.edges.append(edge)
        node.edges.append(edge)

    def reset(self):
        self.visited = False
        self.distance_from_start = 0
        self.distance_to_end = 0
        self.parent = None
        self.referer = None

        for neighbor in self.neighbors:
            neighbor['edge'].visited = False

    def to_dict(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'edges': [edge.to_dict() for edge in self.edges]
        }

    @classmethod
    def from_dict(cls, data):
        node = cls(data['id'], data['latitude'], data['longitude'])
        return node
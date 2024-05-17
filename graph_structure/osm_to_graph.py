import geopandas as gpd
from shapely import Point
from graph_structure.Graph import Graph
import os


def create_graph_from_shapefiles(city):
    directory = r"C:\Users\shafi\PycharmProjects\PathFinder\data"
    city_directory = os.path.join(directory, city)

    streets_path = os.path.join(city_directory, "edges.shp")
    intersections_path = os.path.join(city_directory, "nodes.shp")

    streets = gpd.read_file(streets_path)
    intersections = gpd.read_file(intersections_path)

    g = Graph()


    for idx, row in intersections.iterrows():
        node_id = row['osmid']
        point = row['geometry']
        g.add_node(node_id, point.y, point.x)

    node_lookup = {node.id: node for node in g.nodes.values()}

    for idx, row in streets.iterrows():
        start_node_id = row['u']
        end_node_id = row['v']

        start_node = node_lookup.get(start_node_id)
        end_node = node_lookup.get(end_node_id)

        if start_node and end_node:
            start_node.connect_to(end_node)
            print('Made connection between nodes:', start_node.id, 'and', end_node.id)
        else:
            print('Connection failed for edge:', idx)

    return g

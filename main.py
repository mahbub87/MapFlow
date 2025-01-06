from flask import Flask, render_template, request, jsonify, json
import os

from algorithms.bfs import bfs
from algorithms.bidirectional import bidirectional_search
from algorithms.dfs import dfs
from graph_structure.Graph import Graph
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star
from typing import Optional


app = Flask(__name__)
graph: Optional[Graph] = None
@app.route('/get_city', methods=['POST'])
def get_city():
    global graph  # Reference the global graph variable
    city = request.json.get('city')  # Safely access the 'city' key

    # Define the base directory
    base_directory = r"C:\Users\shafi\PycharmProjects\PathFinder\data"
    city_directory = os.path.join(base_directory, city)

    # Construct the file path for the graph JSON
    file_path = os.path.join(city_directory, 'graph.json')

    graph = Graph.load_from_file(file_path)  # Load graph
    graph_data = graph.to_dict()  # Convert to dict for response
    return jsonify(graph_data)


@app.route('/pathfind', methods=['POST'])
def pathfind():
    global graph

    if graph is None:
        print("Graph not loaded")
        return jsonify({'error': 'Graph not loaded'}), 400

    data = request.get_json()

    if not data or 'start_id' not in data or 'end_id' not in data or 'algorithm' not in data:
        print("Invalid payload")
        return jsonify({'error': 'Invalid request payload'}), 400

    start_id = int(data['start_id'])
    end_id = int(data['end_id'])

    algorithm = data['algorithm']

    if start_id not in graph.nodes or end_id not in graph.nodes:
        print("Invalid node IDs")
        return jsonify({'error': 'Invalid node IDs'}), 400

    # Reset graph
    for node in graph.nodes.values():
        node.reset()
    graph.reset_shortest_path()

    # Perform pathfinding based on the algorithm
    if algorithm == 'dijkstra':
        path = dijkstra(graph, start_id, end_id)
    elif algorithm == 'a_star':
        path = a_star(graph, start_id, end_id)
    elif algorithm == 'bfs':
        path = bfs(graph, start_id, end_id)
    elif algorithm == 'dfs':
        path = dfs(graph, start_id, end_id)
    elif algorithm == 'bi':
        path = bidirectional_search(graph, start_id, end_id)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400

    # Mark edges in the path
    for i in range(len(path) - 1):
        node1_id = path[i]
        node2_id = path[i + 1]
        for edge in graph.nodes[node1_id].edges:
            if (edge.node1.id == node1_id and edge.node2.id == node2_id) or \
                    (edge.node1.id == node2_id and edge.node2.id == node1_id):
                edge.shortestPath = True
                break

    return jsonify({'updatedGraph': graph.to_dict()})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, jsonify, json
import os

from algorithms.bfs import bfs
from algorithms.bidirectional import bidirectional_search
from algorithms.dfs import dfs
from graph_structure.Graph import Graph
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star
from typing import Optional
from flask_compress import Compress  # Enable gzip compression for large JSON responses


app = Flask(__name__)
Compress(app)
graph: Optional[Graph] = None
@app.route('/get_city', methods=['POST'])
def get_city():
    global graph  # Reference the global graph variable
    city = request.json.get('city')  # Safely access the 'city' key

    # Define the base directory relative to the application directory
    base_directory = os.path.join(os.path.dirname(__file__), "data")
    city_directory = os.path.join(base_directory, city)

    # Construct the file path for the graph JSON
    file_path = os.path.join(city_directory, 'graph.json')

    try:
        graph = Graph.load_from_file(file_path)  # Load graph
        graph_data = graph.to_dict()  # Convert to dict for response
        return jsonify(graph_data)
    except FileNotFoundError:
        return jsonify({'error': f'City data for {city} not found.'}), 404



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

    # Perform pathfinding based on the algorithm (get path and visit order)
    if algorithm == 'dijkstra':
        path, visited = dijkstra(graph, start_id, end_id)
    elif algorithm == 'a_star':
        path, visited = a_star(graph, start_id, end_id)
    elif algorithm == 'bfs':
        path, visited = bfs(graph, start_id, end_id)
    elif algorithm == 'dfs':
        path, visited = dfs(graph, start_id, end_id)
    elif algorithm == 'bi':
        path, visited = bidirectional_search(graph, start_id, end_id)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400

    # Return path and visited order for client-side animation
    return jsonify({'path': path, 'visited': visited})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

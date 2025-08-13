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

def _load_graph_for_city(city: str) -> Optional[Graph]:
    if not city:
        return None
    base_directory = os.path.join(os.path.dirname(__file__), "data")
    city_directory = os.path.join(base_directory, city)
    file_path = os.path.join(city_directory, 'graph.json')
    if not os.path.exists(file_path):
        return None
    return Graph.load_from_file(file_path)
@app.route('/get_city', methods=['POST'])
def get_city():
    global graph  # Reference the global graph variable
    city = request.json.get('city')  # Safely access the 'city' key

    # Define the base directory relative to the application directory
    try:
        graph = _load_graph_for_city(city)  # Load graph
        if graph is None:
            raise FileNotFoundError()
        graph_data = graph.to_dict()  # Convert to dict for response
        return jsonify(graph_data)
    except FileNotFoundError:
        return jsonify({'error': f'City data for {city} not found.'}), 404



@app.route('/pathfind', methods=['POST'])
def pathfind():
    global graph

    data = request.get_json()

    if not data or 'start_id' not in data or 'end_id' not in data or 'algorithm' not in data:
        print("Invalid payload")
        return jsonify({'error': 'Invalid request payload'}), 400

    start_id = int(data['start_id'])
    end_id = int(data['end_id'])

    algorithm = data['algorithm']
    # For serverless: load the graph per request based on city
    city = data.get('city')
    if city:
        g = _load_graph_for_city(city)
        if g is None:
            return jsonify({'error': f'City data for {city} not found.'}), 404
    else:
        # Fallback to in-memory graph when running in a persistent server
        g = graph
        if g is None:
            return jsonify({'error': 'Graph not loaded; include "city" in request.'}), 400

    if start_id not in g.nodes or end_id not in g.nodes:
        print("Invalid node IDs")
        return jsonify({'error': 'Invalid node IDs'}), 400

    # Reset graph
    for node in g.nodes.values():
        node.reset()
    g.reset_shortest_path()

    # Perform pathfinding based on the algorithm (get path and visit order)
    if algorithm == 'dijkstra':
        path, visited = dijkstra(g, start_id, end_id)
    elif algorithm == 'a_star':
        path, visited = a_star(g, start_id, end_id)
    elif algorithm == 'bfs':
        path, visited = bfs(g, start_id, end_id)
    elif algorithm == 'dfs':
        path, visited = dfs(g, start_id, end_id)
    elif algorithm == 'bi':
        path, visited = bidirectional_search(g, start_id, end_id)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400

    # Return path and visited order for client-side animation
    return jsonify({'path': path, 'visited': visited})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

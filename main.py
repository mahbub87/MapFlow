from flask import Flask, render_template, request, jsonify
import os

from graph_structure.Graph import Graph

app = Flask(__name__)

@app.route('/get_city', methods=['POST'])
def get_city():
    city = request.json['city']


    print(city)

    directory = r"C:\Users\shafi\PycharmProjects\PathFinder\data" + "\\"
    city_directory = os.path.join(directory, city)
    file_path = os.path.join(city_directory, 'graph.json')
    loaded_graph = Graph.load_from_file(file_path)

    graph_data = loaded_graph.to_dict()
    return jsonify(graph_data)  # Return the graph data as JSON

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

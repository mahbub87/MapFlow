from flask import Flask, render_template, request
import os

from data import osm_data
from graph_structure import visualize_graph
from graph_structure.Graph import Graph
from graph_structure.osm_to_graph import create_graph_from_shapefiles

app = Flask(__name__)


@app.route('/get_city', methods=['POST'])
def get_city():
    city = request.json['city']
    match(city):
        case 'Rome':
            country = 'Italy'
        case 'Chicago':
            country = 'United States'
        case 'Cairo':
            country = 'Egypt'
        case 'Berlin':
            country = 'Germany'
        case 'Paris':
            country = 'France'
        case 'Dhaka Metropolitan':
            country = 'Bangladesh'

    #osm_data.get_osm_data(city, country)
    print(city)
    #g = create_graph_from_shapefiles(city)
    directory = r"C:\Users\shafi\PycharmProjects\PathFinder\data" + "\\"
    city_directory = os.path.join(directory, city)
    file_name = 'graph.json'
    file_path = os.path.join(city_directory, file_name)
    #g.save_to_file(file_path)
    # visualize_graph.visualize_and_save_graph(loaded_graph, 'graph.png')

    loaded_graph = Graph.load_from_file(file_path)

    return country

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

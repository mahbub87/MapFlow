from flask import Flask, render_template, request
import joblib
import os
from graph_structure import visualize_graph
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
        case 'Dhaka':
            country = 'Bangladesh'

    #osm_data.get_osm_data(city, country)
    print(city)
    g = create_graph_from_shapefiles(city)

    visualize_graph.visualize_and_save_graph(g, 'graph.png')
    return country

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

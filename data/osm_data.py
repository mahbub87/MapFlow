import osmnx
import os

def get_osm_data(city, country):
    directory = r"C:\Users\shafi\PycharmProjects\PathFinder\data"+"\\"
    city_directory = os.path.join(directory, city)

    road = osmnx.graph_from_place(city+', '+country,network_type='drive')
    prj_road = osmnx.project_graph(road)

    if not os.path.isdir(city_directory):
        osmnx.save_graph_shapefile(prj_road, filepath=city_directory)

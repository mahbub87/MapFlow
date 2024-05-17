import matplotlib.pyplot as plt

def visualize_and_save_graph(G, output_file):
    plt.figure(figsize=(50, 50))

    # Plot edges
    for node in G.nodes.values():
        for edge in node.edges:
            x_values = [edge.node1.longitude, edge.node2.longitude]
            y_values = [edge.node1.latitude, edge.node2.latitude]
            plt.plot(x_values, y_values, 'b-', linewidth=0.5)

    # Plot nodes
    for node in G.nodes.values():
        plt.plot(node.longitude, node.latitude, 'ro', markersize=0.75)

    plt.title('City Graph')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)

    # Save the plot to a file
    plt.savefig(output_file, bbox_inches='tight')
    print('done!!')
    plt.close()
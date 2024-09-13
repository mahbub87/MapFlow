import matplotlib.pyplot as plt


def visualize_and_save_graph(G, output_file):
    plt.figure(figsize=(50, 50))

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Plot edges with cyan color
    for node in G.nodes.values():
        for edge in node.edges:
            x_values = [edge.node1.longitude, edge.node2.longitude]
            y_values = [edge.node1.latitude, edge.node2.latitude]
            plt.plot(x_values, y_values, 'c-', linewidth=0.5)

    # Plot nodes with red color
    for node in G.nodes.values():
        plt.plot(node.longitude, node.latitude, 'ro', markersize=0)

    # Remove title, xlabel, and ylabel
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')

    # Remove grid if desired
    plt.grid(False)

    # Save the plot to a file
    plt.savefig(output_file, bbox_inches='tight')
    print('done!!')
    plt.close()
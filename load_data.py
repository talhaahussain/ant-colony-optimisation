import xml.etree.ElementTree as ET


def get_distance_matrix(filename):
    """
    Load a distance matrix for a TSP from a TSP XML file.

    Args:
      filename (string): Name of the XML file to load

    Returns:
      distance_matrix ([[int]]): A distance matrix of the cities parsed
    """
    # Parse XML data from the file.
    xml_parser = ET.parse(filename)
    xml_data = xml_parser.getroot()

    # Extract vertex data from the graph fragment of the XML document.
    graph = xml_data.find("graph")
    vertices = graph.findall("vertex")
    num_vertices = len(vertices)

    # Create empty distance matrix.
    distance_matrix = [[0 for i in range(num_vertices)] for i in range(num_vertices)]

    # Iterate through XML fragment.
    for origin, vertex in enumerate(vertices):
        for edge in vertex.findall("edge"):
            # Extact destination/distance data for each vertex.
            destination = int(edge.text)
            distance = int(float(edge.attrib["cost"]))

            # Add distance to the matrix.
            distance_matrix[origin][destination] = distance

    return distance_matrix

# defaultdict because we have duplicate keys
from collections import defaultdict


def read_txt(path_to_file):
    with open(path_to_file, "r") as f:
        input_file = f.readlines()
        input_list = []

        for inputs in range(len(input_file)-1):
            input_str = input_file[inputs][:-1]
            input_list.append(input_str)

        input_list.append(input_file[-1])

    return input_list


def list_to_graph_dict(input_list):
    graph_dict = defaultdict(list)
    temp_list = []

    for inputs in input_list[1:]:
        element = inputs.split(" ")
        temp_list.append(element)

    for keys, values in temp_list:
        graph_dict[keys].append(values)

    return graph_dict


def depth_first_search(input_dict, start_vertex):
    visited = set()

    if start_vertex not in input_dict:
        return None

    def dfs(vertex):
        visited.add(vertex)
        for neighbour in input_dict[vertex]:
            if neighbour not in visited:
                dfs(neighbour)

    dfs(start_vertex)

    return visited


def get_edges(vertices, input_dict):
    edges = []
    for vertex in vertices:
        for neighbour in input_dict[vertex]:
            if (vertex, neighbour) not in edges:
                edges.append((vertex, neighbour))

    return edges


def transpose_graph(input_dict):
    graph_transpose = defaultdict(list)
    for key, value in input_dict.items():
        for item in value:
            graph_transpose[item].append(key)

    return graph_transpose


def get_strongly_connected_components(graph_transpose, vertices):
    scc_list = []
    for vertex in vertices:
        scc_list.append(depth_first_search(graph_transpose, vertex))

    return scc_list


def print_nicely(anything, description):
    print("==================================")
    print(description)
    print("")
    print(anything)
    print("==================================")
    print("")


def main():
    """
    ['12', '1 2', '2 3', '2 4', '2 5', '3 6', '4 5', '4 7', '5 2', '5 6', '5 7',
    '6 3', '6 8', '7 8', '7 10', '8 7', '9 7', '10 9', '10 11', '11 12', '12 10']
    """
    input_list = read_txt("input.txt")

    """
    The adjacency list representation of the graph is as follows:

    defaultdict(<class 'list'>,
    {'1': ['2'], '2': ['3', '4', '5'], '3': ['6'], '4': ['5', '7'], '5': ['2', '6', '7']
    '6': ['3', '8'], '7': ['8', '10'], '8': ['7'], '9': ['7'], '10': ['9', '11'], '11': ['12'], '12': ['10']}
    )

    Here, keys are the edges and values are the vertices.
    """
    input_dict = list_to_graph_dict(input_list)
    print_nicely(input_dict, "Adjacency list representation of the graph")

    # print the dict of vertices in the order of the DFS
    vertices = depth_first_search(input_dict, '1')
    print_nicely(vertices, "The vertices in the order of the DFS")

    # print the list of edges in the order of the DFS
    edges = get_edges(vertices, input_dict)
    # print_nicely(edges, "The edges in the order of the DFS")

    # transpose the input_dict graph
    graph_transpose = transpose_graph(input_dict)
    print_nicely(graph_transpose, "The transpose of the graph")

    # find strongly connected components from input_dict graph
    scc_list = get_strongly_connected_components(input_dict, vertices)
    print_nicely(scc_list, "The strongly connected components")


if __name__ == "__main__":
    main()

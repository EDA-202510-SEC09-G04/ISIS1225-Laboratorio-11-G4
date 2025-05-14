from pprint import pprint
from DataStructures.Map import map_linear_probing as map
from DataStructures.Map import map_entry as me


def new_graph(order, load_factor=0.5):
    graph = {
        'vertices': map.new_map(num_elements=order, load_factor=load_factor),
        'num_edges': 0
    }
    return graph

def insert_vertex(my_graph, key_u, info_u):
    map.put(my_graph['vertices'], key_u, info_u)
    return my_graph

def update_vertex_info(my_graph, key_u, new_info_u):
    my_graph["vertices"] = map.put(my_graph["vertices"], key_u, new_info_u)
    return my_graph

def remove_vertex(my_graph, key_u):
    my_graph["vertices"] = map.remove(my_graph["vertices"], key_u)
    vertices = map.key_set(my_graph["vertices"])
    for key_v in vertices:
        adj = map.get(my_graph["vertices"], key_v)
        if isinstance(adj, dict) and key_u in adj:
            del adj[key_u]
            my_graph["num_edges"] -= 1

    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice u no existe")
    if not contains_vertex(my_graph, key_v):
        raise Exception("El vertice v no existe")

    u = get_vertex(my_graph, key_u)
    
    if u.get('edges') is None:
        u['edges'] = {}

    u['edges'][key_v] = weight
    my_graph['num_edges'] += 1  

    return my_graph


def order(my_graph):
    return my_graph['vertices']['size']

def size(my_graph):
    pass

def vertices(my_graph):
    pass

def degree(my_graph, key_u):
    pass

def get_edge(my_graph, key_u, key_v):
    pass

def get_vertex_information(my_graph, key_u):
    pass

def contains_vertex(my_graph, key_u):
    return map.contains(my_graph['vertices'], key_u)


def adjacents(my_graph, key_u):
    pass

def edges_vertex(my_graph, key_u):
    pass

def get_vertex(my_graph, key_u):
    if not contains_vertex(my_graph, key_u):
        raise Exception("El vertice no existe")

    entry = map.get(my_graph['vertices'], key_u)
    
    return me.get_value(entry)

my_graph = new_graph(1)

my_graph = insert_vertex(my_graph, "Armenia", {"nombre": "Armenia", "poblacion": 300000})
my_graph = insert_vertex(my_graph, "Bogota", {"nombre": "Bogota", "poblacion": 8000000})

my_graph = add_edge(my_graph, "Armenia", "Bogota", 100)

pprint(my_graph)

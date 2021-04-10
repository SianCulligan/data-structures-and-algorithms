from graph import __version__
from graph.graph import Node, Graph, Edge, get_edge

def test_version():
    assert __version__ == '0.1.0'


####### HAPPY PATH ####### 

def test_get_edges():
    graph = Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    naboo = graph.add_node('naboo')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, naboo, 73)
    expected = (True, '$150')
    actual = get_edge(graph, [pandora, arendelle])
    assert actual == expected

####### EDGE CASE ####### 
def test_get_edges_with_a_city_outside_graph():
    graph = Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    naboo = graph.add_node('naboo')
    zootopia = graph.add_node('zootopia')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, naboo, 73)
    expected = (False, '$0')
    actual = get_edge(graph, [pandora, zootopia])
    assert actual == expected


# ####### EXPECTED FAIL ####### 
def test_get_edges_with_cities_that_do_not_connect():
    graph = Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    naboo = graph.add_node('naboo')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, naboo, 73)
    expected = (False, '$0')
    actual = get_edge(graph, [pandora, naboo])
    assert actual == expected
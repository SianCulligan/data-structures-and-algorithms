from graph import __version__
from graph.graph import Node, Graph, Edge


def test_version():
    assert __version__ == '0.1.0'


####### HAPPY PATH ####### 

def test_breadth_first_traversal():
    graph = Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    naboo = graph.add_node('naboo')
    graph.add_edge(pandora, arendelle)
    graph.add_edge(arendelle, metroville)
    graph.add_edge(metroville, naboo)
    expected = ['pandora', 'arendelle', 'metroville', 'naboo']
    actual = graph.breadth_first_traversal(pandora)
    assert actual == expected

####### EDGE CASE ####### 
def test_breadth_first_traversal_with_unattached_node():
    graph = Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    naboo = graph.add_node('naboo')
    zootopia = graph.add_node('zootopia')
    graph.add_edge(pandora, arendelle)
    graph.add_edge(arendelle, metroville)
    graph.add_edge(metroville, naboo)
    expected = ['pandora', 'arendelle', 'metroville', 'naboo']
    actual = graph.breadth_first_traversal(pandora)
    assert actual == expected


####### EXPECTED FAIL ####### 
def test_breadth_first_traversal_with_empty_graph():
    graph = Graph()
    expected = "Error"
    actual = graph.breadth_first_traversal()
    assert actual == expected

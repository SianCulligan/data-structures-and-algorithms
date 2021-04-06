from depth_first import __version__
from depth_first.depth_first import Graph, Node, Edge

def test_version():
    assert __version__ == '0.1.0'


############ HAPPY PATH ############
def test_with_valid_adj_list():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')

    expected = ['a', 'b', 'c']
    actual = graph.depth_first(a)
    assert expected == actual

############ EDGE CASE ############
def test_with_empty_list():
    graph = Graph()

    expected = 'Starting point not in list'
    actual = graph.depth_first(graph)
    assert expected == actual

############ EXPECTED FAIL ############
def test_with_parameter_that_does_not_exist():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')


    expected = 'Starting point not in list'
    actual = graph.depth_first(graph)
    assert expected == actual
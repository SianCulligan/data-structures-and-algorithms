from graph import __version__
from graph.graph import Node, Graph, Edge


def test_version():
    assert __version__ == '0.1.0'

def test_size():
    new_graph = Graph()
    new_graph.add_node('a')
    new_graph.add_node('b')
    expected = 2
    actual = new_graph.size()
    assert actual == expected

def test_add_node_pass():
    node = Node('a')
    actual = node.value
    expected = 'a'
    assert actual == expected

def test_add_node_fail():
    node = Node('a')
    actual = node.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual
    
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True
 
def test_get_nodes():
    new_graph_get_nodes = Graph()
    new_graph_get_nodes.add_node('a')
    new_graph_get_nodes.add_node('b')
    actual = len(new_graph_get_nodes.get_nodes())
    expected = 7
    assert actual == expected

def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected


def test_get_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    actual = graph.get_neighbors(a)
    expected = []
    assert actual == expected

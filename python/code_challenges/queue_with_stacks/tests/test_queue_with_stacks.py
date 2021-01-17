from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue, Stack


def test_version():
    assert __version__ == '0.1.0'

def test_can_successfully_enqueue():
    new_queue = PseudoQueue()
    new_queue.enqueue(5)

    expected = 5
    actual = new_queue.front.nodeVal

    assert expected == actual

def test_can_successfully_enqueue_multiple_nodes():
    new_queue = PseudoQueue()
    new_queue.enqueue(5)
    new_queue.enqueue(10)
    new_queue.enqueue(15)
    new_queue.enqueue(20)

    expected = 20
    actual = new_queue.front.nodeVal

    assert expected == actual

def test_can_successfully_dequeue():
    new_queue = PseudoQueue()
    new_queue.enqueue(5)
    expected = 5
    actual = new_queue.dequeue()

    assert expected == actual

def test_can_successfully_throw_a_dequeue_exception():
    new_queue = PseudoQueue()
    expected = "Exception"
    actual = new_queue.dequeue()
    assert expected == actual    

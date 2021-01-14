from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Node, Stack, Queue


def test_version():
    assert __version__ == '0.1.0'

#**************STACK TESTS**************

# Can successfully instantiate an empty stack
def test_can_successfully_instantiate_an_empty_stack():
    new_stack = Stack()
    expected = None
    actual = new_stack.top
    assert expected == actual

# Can successfully push onto a stack
def test_can_successfully_push_to_a_stack():
    new_stack = Stack()
    new_stack.push('blue');
    expected = 'blue'
    actual = new_stack.peek()
    assert expected == actual

# Can successfully push multiple values onto a stack
def test_can_successfully_push_multiple_values_onto_a_stack():
    new_stack = Stack()
    new_stack.push('blue');
    new_stack.push('red');
    new_stack.push('orange');
    new_stack.push('green');

    expected = 'green'
    actual = new_stack.peek()
    assert expected == actual    

# Can successfully pop off the stack
def test_can_successfully_pop_from_a_stack():
    new_stack = Stack()
    new_stack.push('red');
    new_stack.push('orange');
    new_stack.push('green');
    new_stack.push('blue');

    new_stack.pop()

    expected = 'green'
    actual = new_stack.peek()
    assert expected == actual

# Can successfully empty a stack after multiple pops
def test_can_successfully_empty_a_stack_after_multiple_pops():
    new_stack = Stack()
    new_stack.push('red');
    new_stack.push('orange');
    new_stack.push('green');
    new_stack.push('blue');

    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()

    expected = True
    actual = new_stack.isempty()
    assert expected == actual   

# Can successfully peek the next item on the stack
def test_can_successfully_peek_the_stack():
    new_stack = Stack()
    new_stack.push('green');
    new_stack.push('blue');

    expected = 'blue'
    actual = new_stack.peek()
    assert expected == actual

# Calling pop or peek on empty stack raises exception
def test_pop_on_empty_raises_exception():
    new_stack = Stack()
    expected = 'Exception'
    actual = new_stack.pop()
    assert expected == actual   

def test_peek_on_empty_raises_exception():
    new_stack = Stack()
    expected = 'Exception'
    actual = new_stack.peek()
    assert expected == actual  

    
#**************QUEUE TESTS**************







# Can successfully enqueue into a queue
def test_can_successfully_enqueue_into_a_queue():
    new_queue = Queue()
    new_queue.enqueue('One');
    expected = 'One'
    actual = new_queue.peek()
    assert expected == actual


# Can successfully instantiate an empty queue
def test_can_successfully_instantiate_an_empty_queue():
    new_queue = Queue()
    expected = None
    actual = new_queue.front
    assert expected == actual


# Can successfully enqueue multiple values into a queue
def test_can_successfully_enqueue_multiple_values_into_a_queue():
    new_queue = Queue()
    new_queue.enqueue('Three');
    new_queue.enqueue('Two');
    new_queue.enqueue('One');
    expected = 'Three'
    actual = new_queue.peek()
    assert expected == actual

# Can successfully dequeue out of a queue the expected value
def test_can_successfully_dequeue_out_of_a_queue_the_expected_value():
    new_queue = Queue()
    new_queue.enqueue('Three');
    new_queue.enqueue('Two');
    new_queue.enqueue('One');
    expected = 'Three'
    actual = new_queue.peek()
    assert expected == actual

# Can successfully peek into a queue, seeing the expected value
def test_can_successfully_peek_into_a_queue_seeing_the_expected_value():
    new_queue = Queue()
    new_queue.enqueue('Three');
    expected = 'Three'
    actual = new_queue.peek()
    assert expected == actual

# Can successfully empty a queue after multiple dequeues
def test_can_successfully_empty_a_queue_after_multiple_dequeues():
    new_queue = Queue()
    new_queue.enqueue('One');
    new_queue.enqueue('Two');
    new_queue.enqueue('Three');
    new_queue.enqueue('Four');

    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()
    new_queue.dequeue()

    expected = True
    actual = new_queue.isempty()
    assert expected == actual   

# Calling dequeue or peek on empty queue raises exception

def test_peek_on_empty_raises_exception():
    new_queue = Queue()
    expected = 'Exception'
    actual = new_queue.peek()
    assert expected == actual   

def test_dequeue_on_empty_raises_exception():
    new_queue = Queue()
    expected = 'Exception'
    actual = new_queue.dequeue()
    assert expected == actual  

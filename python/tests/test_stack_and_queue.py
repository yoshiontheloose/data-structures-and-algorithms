from inspect import stack
import queue
import pytest

from code_challenges.stack_and_queue.node import Node
from code_challenges.stack_and_queue.queue import Queue
from code_challenges.stack_and_queue.stack import Stack


# Can successfully push onto a stack
# @pytest.mark.skip('Pending')
def test_stack_single_push():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1


# Can successfully push multiple values onto a stack
# @pytest.mark.skip('Pending')
def test_stack_multi_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.value == 3
    # assert stack.top.value != 2 (another way/extra validation)


# Can successfully pop off the stack
# @pytest.mark.skip('Pending')
def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.pop()
    expected = 3
    assert expected == actual


# Can successfully empty a stack after multiple pops
# @pytest.mark.skip('Pending')
def test_stack_empty_multi_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    with pytest.raises(Exception):
        stack.pop()
    assert stack.is_empty() == True

# Can successfully peek the next item on the stack
# @pytest.mark.skip('Pending')
def test_stack_peek():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.peek()
    expected = 3
    assert expected == actual

# Can successfully instantiate an empty stack
# @pytest.mark.skip('Pending')
def test_stack_empty():
    stack = Stack()
    assert stack.is_empty() == True

# Calling pop or peek on empty stack raises exception
# @pytest.mark.skip('Pending')
def test_stack_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()
    with pytest.raises(Exception):
        stack.pop()

# -------------------------------------

# Can successfully enqueue into a queue
# @pytest.mark.skip('Pending')
def test_queue_enqueue_single():
    queue = Queue()
    queue.enqueue(1)
    expected = 1
    actual = queue.rear.value
    assert expected == actual

# Can successfully enqueue multiple values into a queue
# @pytest.mark.skip('Pending')
def test_queue_enqueue_multi():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual_front = queue.front.value
    actual_next = queue.front.next.value
    actual_rear = queue.rear.value
    assert actual_front == 1
    assert actual_next == 2
    assert actual_rear == 3

# Can successfully dequeue out of a queue the expected value
# @pytest.mark.skip('Pending')
def test_queue_dequeue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 1
    actual = queue.dequeue()
    assert expected == actual
    assert queue.front.value == 2

# Can successfully peek into a queue, seeing the expected value
# @pytest.mark.skip('Pending')
def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 1
    actual = queue.peek()
    assert expected == actual

# Can successfully empty a queue after multiple dequeues
# @pytest.mark.skip('Pending')
def test_queue_empty_multi():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    with pytest.raises(Exception):
        queue.peek()
    assert queue.is_empty() == True


# Can successfully instantiate an empty queue
# @pytest.mark.skip('Pending')
def test_queue_empty():
    queue = Queue()
    assert queue.is_empty() == True


# Calling dequeue or peek on empty queue raises exception
# @pytest.mark.skip('Pending')
def test_queue_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()
    with pytest.raises(Exception):
        queue.peek()

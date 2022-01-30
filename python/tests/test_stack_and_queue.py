from inspect import stack
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
    assert stack.is_empty() == False
    stack.pop()
    with pytest.raises(Exception):
        stack.pop()
    assert stack.is_empty() == True

# Can successfully peek the next item on the stack
@pytest.mark.skip('Pending')
def test_stack_peek():
    pass


# Can successfully instantiate an empty stack
@pytest.mark.skip('Pending')
def test_stack_empty():
    pass


# Calling pop or peek on empty stack raises exception
@pytest.mark.skip('Pending')
def test_stack_empty_exception():
    pass


# Can successfully enqueue into a queue
@pytest.mark.skip('Pending')
def test_queue_enqueue_single():
    pass


# Can successfully enqueue multiple values into a queue
@pytest.mark.skip('Pending')
def test_queue_enqueue_multi():
    pass


# Can successfully dequeue out of a queue the expected value
@pytest.mark.skip('Pending')
def test_queue_dequeue():
    pass


# Can successfully peek into a queue, seeing the expected value
@pytest.mark.skip('Pending')
def test_queue_peek():
    pass


# Can successfully empty a queue after multiple dequeues
@pytest.mark.skip('Pending')
def test_queue_empty_multi():
    pass


# Can successfully instantiate an empty queue
@pytest.mark.skip('Pending')
def test_queue_empty():
    pass


# Calling dequeue or peek on empty queue raises exception
@pytest.mark.skip('Pending')
def test_queue_empty_exception():
    pass

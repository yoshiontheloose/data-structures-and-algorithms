import pytest
from linked_list.linked_list import LinkedList, Node

# testing what the node knows. Empty Node

@pytest.mark.skip('Pending')
def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

# testing empty node fails, prevents false positive tests
@pytest.mark.skip('Pending')
def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

# head creation
@pytest.mark.skip('Pending')
def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

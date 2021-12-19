from linked_list.linked_list import LinkedList, Node

# testing what the node knows. Empty Node
def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1

# testing empty node fails, prevents false positive tests
def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2

# head creation
def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node

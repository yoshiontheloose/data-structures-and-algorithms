from re import L
from unittest import result
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

# Can successfully instantiate an empty linked list
def test_empty_ll():
    ll = LinkedList()
    assert ll.head == None

# Can properly insert into the linked list
def test_insert():
    ll = LinkedList()
    ll.insert('a')
    assert ll.head.value == 'a'


# The head property will properly point to the first node in the linked list
def test_head_to_first_node():
    ll = LinkedList()
    head = Node('head')
    ll.head = head
    first_node = Node('first')
    ll.head.next = first_node
    assert ll.head.next.value == 'first'


# Can properly insert multiple nodes into the linked list
def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert('a')
    assert ll.head.value == 'a'
    ll.insert('b')
    assert ll.head.value == 'b'
    assert ll.head.next.value == 'a'
    ll.insert('c')
    assert ll.head.value == 'c'
    assert ll.head.next.value == 'b'

# Will return true when finding a value within the linked list that exists
def test_ll_value_true():
    ll = LinkedList()
    ll.insert('a')
    result = ll.includes('a')
    assert result == True

# Will return false when searching for a value in the linked list that does not exist
def test_ll_value_false():
    ll = LinkedList()
    ll.insert('a')
    result = ll.includes('b')
    assert result == False

# Can properly return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    assert ll.__str__() == 'c -> b -> a -> NULL'

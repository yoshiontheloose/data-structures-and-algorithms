
from cgitb import reset


class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Create a Linked List class, include a head property
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

# Arguments: value
# Adds a new node with that value to the head of the list with an O(1) Time performance.
# Returns: nothing

# if there is a head in the LL, the next node will be the head
    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

# Arguments: value
# Indicates whether that value exists as a Node’s value somewhere within the list.
# Returns: Boolean

# start with the LL head, check for head,
# if there is a head value, the value returns true,
# then current is reassigned to next
# returns false if head value is None
    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

# Arguments: none
# Returns: a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"

# make an empty string for string to be returned
# while there is a head,
# the current head value in string form will add to the result string
# else if no head, NULL will be put into result string
    def __str__(self):
        result_string = ''
        current = self.head
        while current:
            result_string += f'{current.value} -> '
            current = current.next
        else:
            result_string += 'NULL'
        return result_string


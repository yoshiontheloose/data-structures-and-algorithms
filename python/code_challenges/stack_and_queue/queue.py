# from node import Node

class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next


# First In First Out | Last In Last Out

# Create a Queue class that has a front property. It creates an empty Queue when instantiated.
# This object should be aware of a default empty value assigned to front when the queue is created.

class Queue:
    def __init__(self, front= None, rear= None):
        self.front = front
        self.rear = rear


# The class should contain the following methods:

# enqueue
# Arguments: value
# adds a new node with that value to the back of the queue with an O(1) Time performance.

    def enqueue(self, value):
        new_node = Node(value)
        if new_node is True:
            new_node = self.rear


# dequeue
# Arguments: none
# Removes the node from the front of the queue
# Should raise exception when called on empty queue
# Returns: the value from node from the front of the queue

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self.next = self.front
        return self.front.value


# peek
# Arguments: none
# Should raise exception when called on empty stack
# Returns: Value of the node located at the front of the queue

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

# is empty
# Arguments: none
# Returns: Boolean indicating whether or not the queue is empty

    def is_empty(self):
        return self.front == None

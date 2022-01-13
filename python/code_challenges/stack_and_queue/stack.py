from stack_and_queue.node import Node

# Create a Stack class that has a top property.
# It creates an empty Stack when instantiated.
# This object should be aware of a default empty value assigned to top when the stack is created.
class Stack:
    def __init__(self, top=None):
        self.top = top

# The class should contain the following methods:
# push
# Arguments: value
# adds a new node with that value to the top of the stack with an O(1) Time performance.
    def push(self, value):
        node = Node(value)
        









# pop
# Arguments: none
# Returns: the value from node from the top of the stack
# Removes the node from the top of the stack
# Should raise exception when called on empty stack

# peek
# Arguments: none
# Returns: Value of the node located at the top of the stack
# Should raise exception when called on empty stack

# is empty
# Arguments: none
# Returns: Boolean indicating whether or not the stack is empty

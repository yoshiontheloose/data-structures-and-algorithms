from stack_and_queue.node import Node


class Node:
    def __init__(self, value, above= None):
        self.value = value
        self.above = above

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


# make a push function that takes a value
    def push(self, value):
#  create a node with a value
        new_node = Node(value)
# Check stack for a Top
# if true
        if self.top is True:
#  Add new node as the next of top
            new_node.next = self.top
# Assign Node to the Top
            self.top = new_node
        else:
# Assign Node to the Top
            self.top = new_node


# pop
# Arguments: none
# Returns: the value from node from the top of the stack
# Removes the node from the top of the stack
# Should raise exception when called on empty stack

    def pop(self):
        # check if stack is empty
        if self.top is None:
    # raise exception
            print("stack is empty")
# assign current_top to return_value
            return_value = self.top
# reassign top of stack to the current top's next value
            self.top = return_value.next
# return the return_value
            return return_value


# peek
# Arguments: none
# Returns: Value of the node located at the top of the stack
# Should raise exception when called on empty stack





# is empty
# Arguments: none
# Returns: Boolean indicating whether or not the stack is empty

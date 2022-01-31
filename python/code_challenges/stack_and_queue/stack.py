from code_challenges.stack_and_queue.node import Node

# class Node:
#     def __init__(self, value, next= None):
#         self.value = value
#         self.next = next

# Create a Stack class that has a top property.
# It creates an empty Stack when instantiated.
# This object should be aware of a default empty value assigned to top when the stack is created.
class Stack:
    def __init__(self, top=None):
        self.top = top

# push
# Arguments: value
# adds a new node with that value to the top of the stack with an O(1) Time performance.

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

# pop
# Arguments: none
# Removes the node from the top of the stack
# Returns: the value from node from the top of the stack
# Should raise exception when called on empty stack

    def pop(self):
        if self.is_empty() is False:
            new_top = self.top
            self.top = new_top.next
            return new_top.value
        else:
            raise Exception("Stack is empty")

# peek
# Arguments: none
# Should raise exception when called on empty stack
# Returns: Value of the node located at the top of the stack

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        else:
            return self.top.value

# is empty
# Arguments: none
# Returns: Boolean indicating whether or not the stack is empty

    def is_empty(self):
        return self.top == None

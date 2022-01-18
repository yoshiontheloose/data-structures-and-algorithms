# Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
# (Using above as next)

class Node:
    def __init__(self, value, above= None):
        self.value = value
        self.above = above

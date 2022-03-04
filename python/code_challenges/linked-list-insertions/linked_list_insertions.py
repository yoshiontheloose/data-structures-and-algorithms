class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        # initialization here
        self.head = head


    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node


    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False


    def __str__(self):
        result_string = ''
        current = self.head
        while current:
            result_string += f'{current.value} -> '
            current = current.next
        else:
            result_string += 'NULL'
        return result_string


# append method
# argument: new value
# adds a new node with the given value to the end of the list

    def append(new_value):





# insert before method
# arguments: value, new value
# adds a new node with the given new value immediately before the first node that has the value specified




# insert after method
# arguments: value, new value
# adds a new node with the given new value immediately after the first node that has the value specified

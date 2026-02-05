
# Data structures begin
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially, this node points to nothing

class LinkedList:
    def __init__(self):
        self.head = None

    # O(1) complexity - Very fast
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # O(n) complexity - Must walk to the end
    def insert_at_end(self, data):
        new_node = Node(data)
        # if the list is empty add the new_node and return
        if not self.head:
            self.head = new_node
            return
        # if the list is not empty go to the last node
        #   and add the new_node at the end
        current = self.head
        # while there is next node, move to it
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        # while there is data, get it and go to next
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" --> ".join(elements) + " --> None")
# Data structures end
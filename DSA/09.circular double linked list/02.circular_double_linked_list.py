class Node:

    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList:

    def __init__(self, value=None):
        if value is None:       # if value is not given create empty cdlinkedlist
            self.head = None
            self.tail = None
            self.length = 0
        else:                   # if value is given create cdlinkedlist with one node
            new_node = Node(value)
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
            self.length = 1
        




cdll=CircularDoublyLinkedList(7)

print(cdll.head)
print(cdll.head.prev)
print(cdll.tail)
print(cdll.tail.next)
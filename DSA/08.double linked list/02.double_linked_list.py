class Node:

    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:

    def __init__(self,value):
        new_node=Node(value)
        self.head=None
        self.tail=None
        self.length=0
        

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1



dll=DoublyLinkedList(7)
dll.append(10)
dll.append(20)
print(dll.head)
print(dll.tail)
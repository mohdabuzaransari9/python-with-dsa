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


    def append(self,value):
        '''
        case 1: if it is empty circular doubly linked list
        case 2: if non empty circular doubly linked list exist
        
        '''

        new_node=Node(value)

        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail=new_node

        self.length+=1
        
    
    def __str__(self):
        current_node=self.head
        result=""
        while current_node:
            result+=str(current_node.value)
            current_node=current_node.next
            if current_node==self.head:
                break
            result+=" <-> "

        return result
    
    def prepend(self,value):
        '''
        case 1: if it is empty circular doubly linked list
        case 2: if non empty circular doubly linked list exist
        '''
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node    
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.head=new_node

        self.length+=1
        
        




cdll=CircularDoublyLinkedList()

print("append")
cdll.append(10)
cdll.append(20)
print(cdll.head)


print("__str__")
cdll2=CircularDoublyLinkedList()
cdll2.append(10)
cdll2.append(20)
print(cdll2)


print("prepend")
cdll3=CircularDoublyLinkedList()
cdll3.append(10)
cdll3.append(20)
cdll3.prepend(20)
print(cdll3)
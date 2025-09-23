class Node:

    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:

    def __init__(self, value=None):
        if value is None:       # if value is not given create empty cslinkedlist
            self.head = None
            self.tail = None
            self.length = 0
        else:                   # if value is given create cslinkedlist with one node
            new_node = Node(value)
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
            self.length = 1
        

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

    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node:
            result+=str(temp_node.value)
        
            if temp_node.next:
                result+= " <-> "
            temp_node=temp_node.next
        return result
    

    def prepend(self,value):
        '''
        case1= empty node
        case2= double linked list exist

        '''
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            
            
        self.length+=1

    def traverse(self):
        current_node=self.head
        while current_node:
            print(current_node.value)
            current_node=current_node.next

            



dll=DoublyLinkedList(7)
dll.append(10)
dll.append(20)
print(dll.head)
print(dll.tail)

print("__str__")
dll1 = DoublyLinkedList(1)       
dll1.append(5)
dll1.append(10)
dll1.append(20)
print(dll1) 

print("prepend")
dll2 = DoublyLinkedList(1)       
dll2.append(5)
dll2.append(10)
dll2.prepend(20)
print(dll2) 

print("traverse")
dll3 = DoublyLinkedList(1)       
dll3.append(5)
dll3.append(10)
dll3.prepend(20)
print(dll3) 
dll3.traverse()
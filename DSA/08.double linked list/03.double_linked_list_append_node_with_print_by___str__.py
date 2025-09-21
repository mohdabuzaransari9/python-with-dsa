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

    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node:
            result+=str(temp_node.value)
        
            if temp_node.next:
                result+= " <-> "
            temp_node=temp_node.next
        return result
            



dll=DoublyLinkedList(7)
dll.append(10)
dll.append(20)
print(dll.head)
print(dll.tail)

print("__str__")
dll1 = DoublyLinkedList(6)       
dll1.append(5)
dll1.append(10)
dll1.append(20)
print(dll1) 
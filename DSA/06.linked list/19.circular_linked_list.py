class Node:
    
    def __init__(self,value):
            self.value=value
            self.next=None

class CSLinkedList:
      

    # def __init__(self):
    
    #     self.head=None
    #     self.tail=None
    #     self.length=0


    # def __init__(self,value):
    #     new_node=Node(value)
    #     new_node.next=new_node
    #     self.head=new_node
    #     self.tail=new_node
    #     self.length=1


    
    
    # combining functions 

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


print("empty CSLinkedList")
cslinkedlist1 = CSLinkedList()         
print(cslinkedlist1.head)  

print("one node CSLinkedList")
cslinkedlist2 = CSLinkedList(10)       
print(cslinkedlist2.head.value)  
print(cslinkedlist2.head.next.value)  


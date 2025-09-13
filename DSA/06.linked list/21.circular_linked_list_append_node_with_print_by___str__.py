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

    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            
            if temp_node==self.head:
                break
            result+=" -> "
            
        return result
        




    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1


print("empty CSLinkedList")
cslinkedlist1 = CSLinkedList()         
print(cslinkedlist1.head)  

print("one node CSLinkedList")
cslinkedlist2 = CSLinkedList(10)       
print(cslinkedlist2.head.value)  
print(cslinkedlist2.head.next.value)  

print("append")
cslinkedlist3 = CSLinkedList()       
cslinkedlist3.append(5)
cslinkedlist3.append(10)
print(cslinkedlist3.head.value)  
print(cslinkedlist3.tail.value)  
  

print("__str__")
cslinkedlist4 = CSLinkedList()       
cslinkedlist4.append(5)
cslinkedlist4.append(10)
cslinkedlist4.append(20)
print(cslinkedlist4) 
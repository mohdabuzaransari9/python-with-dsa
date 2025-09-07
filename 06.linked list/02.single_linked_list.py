class Node:
    def __init__(self,value):
        self.value=value
        self.next=None




class LinkedList:

    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

new_linked_List=LinkedList(5)        
print(new_linked_List)
print(new_linked_List.head.value)
print(new_linked_List.tail.value)
print(new_linked_List.length)
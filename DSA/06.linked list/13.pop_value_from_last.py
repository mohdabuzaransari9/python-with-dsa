class Node:
    def __init__(self,value):
        self.value=value
        self.next=None




class LinkedList:

    def __init__(self):
        
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp_node=self.head
        result= ''
        while temp_node is not None:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result +=' -> '
            temp_node=temp_node.next
    
        return  result
    

    def append(self,value):

        new_node=Node(value)
        if self.head is None:

            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            self.tail= new_node

            
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def insert(self,index,value):
        new_node=Node(value)

        if index<0 or index>self.length:         #  negative edge case orout of range edge case
            return False
        elif self.length==0:                     # empty linkedlist
            self.head=new_node
            self.tail=new_node

        elif index==0:                          # 0th index linkedlist
            new_node.next=self.head
            self.head=new_node

        else:                                   # else
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node

            

        self.length+=1
        return True
    
    def traverse(self):
        current=self.head
        while current:  # while current is not None
            print(current.value)
            current=current.next

    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value==target:
                print(current.value)
                return index
            current=current.next
            index+=1
        return -1

    def get(self, index):

        if index==-1:
            return self.tail
        if index<-1 or index >= self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current
    
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    

    def pop_first(self):

        if self.length==0:  #edge case if linked list empty
            return None

        if self.length==1:         #edge case if linked list only one node
            self.head=None
            self.tail=None
            return popped_node
        
        else:
            popped_node=self.head
            self.head=self.head.next
            popped_node.next=None

        self.length-=1
        return popped_node
    

    def pop(self):

        if self.length==0:
            return None

        popped_node=self.tail

        if self.length==1:
            # self.head=None          # just to learn pythonic tactics
            # self.tail=None
            self.head=self.tail=None        #pythonic tactic
         
        
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
        self.length-=1
        return popped_node



        


new_linked_List=LinkedList() 
new_linked_List.prepend(10)   
new_linked_List.append(20)
print(new_linked_List)
new_linked_List.prepend(5)   
print(new_linked_List)
new_linked_List.insert(2,100)   # insert middle
print(new_linked_List)
new_linked_List.insert(0,1)   # insert beginning
print(new_linked_List)

new_linked_List.insert(100,1000)   # insert end edge case out of range

if new_linked_List!=new_linked_List:
    print(new_linked_List)


new_linked_List.traverse()
print(new_linked_List.search(140))


print(new_linked_List.search(140))

print(new_linked_List)
print(new_linked_List.get(2))

print(new_linked_List)
print(new_linked_List.set(6,200))

print("\npop_first example")
print(new_linked_List)
print(new_linked_List.pop_first())
print(new_linked_List)

print("\npop example")
print(new_linked_List)
print(new_linked_List.pop())
print(new_linked_List)

class Node:
    
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        


class LinkedList:
    def __init__(self):
        self.head=None
        
 # insertion method for the linked list
    def create(self, data):
      newNode = Node(data)
      
      if(self.head):
        current = self.head
        while(current.next):
         current = current.next
        current.next = newNode
      else:
        self.head = newNode
        
  # insertion method for the linked list
    def insert_pos(self, data,pos):
      newNode = Node(data)
      
      if(pos == 1):
          newNode.next = self.head
          self.head = newNode
      else:
          current = self.head
          for i in range(1,pos-1):
              current = current.next
              
          newNode.next = current.next
          current.next = newNode
    
# deletion method for the linked list
    def delete_pos(self, pos):
     
      
      if(pos == 1):
          current = self.head
          self.head = self.head.next    
      else:
          current = self.head
          for i in range(1,pos):
              
              prev = current
              current = current.next
          prev.next = current.next
      current = None        
          

        
  # print method for the linked list
    def printLL(self):
      current = self.head
      while(current):
        print(current.data)
        current = current.next

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.create(3)
LL.create(4)
LL.create(5)
LL.create(6)
LL.create(7)
LL.printLL()

print("*************")
'''
LL.insert_pos(10,1)
LL.insert_pos(25,3)
LL.printLL()
LL.delete_pos(4)
LL.printLL()
'''
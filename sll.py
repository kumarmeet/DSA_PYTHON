class Node:
  def __init__(self,value):
    self.value = value
    self.next = None


class SLL:
  def __init__(self):
    self.head = None
  
  def append(self, value):
    new_node = Node(value)
    
    if self.head == None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      temp.next = new_node
  
  def insert_at_beginning(self, value):
    new_node = Node(value)
    first_node = self.head
    new_node.next = first_node
    self.head = new_node
    del first_node
      
  def traversal(self):
    if(self.head == None):
      print("List is empty")
    else:
      temp = self.head
      while temp != None:
        print(temp.value)
        temp = temp.next
  
  def delete_last_node(self):
    if self.head is None:
      print("List is empty")
    elif not self.head.next:
      self.head = None
    else:
      temp = self.head
      while temp.next.next is not None:
        temp = temp.next
      temp.next = None
      
      
sll = SLL()

sll.append(10)
sll.append(20)
sll.append(30)
sll.insert_at_beginning(40)
sll.insert_at_beginning(44)

# ssl.delete_last_node()
# ssl.delete_last_node()
# ssl.delete_last_node()

ssl.traversal()

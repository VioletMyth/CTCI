class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
class LinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1
  
  def append(self, value): #add to end of list O(1)
    newNode = Node(value)
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1
  
  def preappend(self,value): #add to front of list O(1)
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode
    self.length += 1

  def insert(self, value, index): #add in middle of list O(n) because we need to find the ith node
    curr = self.head
    newNode = Node(value)
    i = 0
    while i < index - 1:
      curr = curr.next
      i += 1
    newNode.next = curr.next
    curr.next = newNode
    self.length += 1

  def remove(self, index): #remove in the middle of the list O(n) because we need to find the ith node
    curr = self.head
    i = 0
    while i < index - 1:
      curr = curr.next
      i += 1
    curr.next = curr.next.next

  
  def printVals(self):
    curr = self.head
    while curr:
      print(curr.value)
      curr = curr.next
  
  def reverse(self):  #O(n) time because we have to loop throguh the entire list.
    previous = None
    current = self.head
    while current:
      temp = current.next
      current.next = previous
      previous = current
      current = temp
    self.head = previous


myLinkedList = LinkedList(10)
myLinkedList.append(12)
myLinkedList.append(13)
myLinkedList.append(14)
myLinkedList.printVals()
myLinkedList.reverse()
print("reversed")
myLinkedList.printVals()

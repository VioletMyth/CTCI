class myDynamicArray:
  def __init__(self):
    self.len = 0    #tracks the length of array
    self.data = []  #items in array
  
  def append(self, data): #append to end
    self.data.append(data)
    self.len += 1

  def get(self, index): #get item at index
    return self.data[index]
  
  def pop(self):  #remove last item in list
    lastItem = self.data[-1]
    del self.data[-1]
    self.len -= 1
    return lastItem

  def delete(self, index):  #remove item at index in list
    self.data.pop(index)
    self.len -= 1

  def length(self): #return list length
    return self.len

  def __repr__(self): #representation of object
    string = "["
    for item in self.data:
      string += str(item) + " ,"
    string = string[:-2]
    return string + "]"

list1 = myDynamicArray()
list1.append(1)
list1.append(2)
list1.pop()
print(list1.length())
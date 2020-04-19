class HashTable:
  def __init__(self,size):
    self.data = [None] * size

  def hash(self, key):  #no collision resolution, previous data is erased when there is a collision
    hashing = 0
    for i in range(len(key)):
      hashing = (hashing + ord(key[i]) * i) % len(self.data)
    return hashing
  
  def set(self, key, value):
    slot = self.hash(key)
    self.data[slot] = [key, value]
  
  def get(self, key):
    slot = self.hash(key)
    return self.data[slot][-1]

  
myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))

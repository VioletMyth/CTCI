#time complexity - O(n)
#space complexity - O(n)
"""def FirstRecurrChar(inputList):
  seenMap = set()
  for char in inputList:
    if char in seenMap:
      return True
    seenMap.add(char)
  return False"""

#brute force approach
#time complexity - O(n^2)
#space complexity - O(1)
def FirstRecurrChar2(inputList):
  for i in range(len(inputList)):
    for j in range(i + 1, len(inputList)):
      if compare(i,j, inputList):
        return True
  return False

def compare(index1, index2, inputList):
  return inputList[index1] == inputList[index2]

print(FirstRecurrChar2([1,2,3,1]))
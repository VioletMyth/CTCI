#time complexity - O(n)
#space complexity - O(n)
def FirstRecurrChar(inputList):
  seenMap = set()
  for char in inputList:
    if char in seenMap:
      return char
    seenMap.add(char)
  return False

#brute force approach so it returns the first seen recurring character
#time complexity - O(n^2)
#space complexity - O(1)
def FirstRecurrChar2(inputList):
  earliest = float('inf')
  for i in range(len(inputList)):
    for j in range(i + 1, len(inputList)):
      if compare(i,j, inputList):
        if j < earliest:
          earliest = j
  if earliest == float('inf'):
    return False
  else:
    return inputList[earliest] 

def compare(index1, index2, inputList):
  return inputList[index1] == inputList[index2]
print(FirstRecurrChar([]))
print(FirstRecurrChar2([2,5,5]))
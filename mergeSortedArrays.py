def mergeSortedArray(array1, array2):
  output = []
  while array1 and array2:  #append everything to output from smallest list and compare only till length of smallest array
    if array1[0] < array2[0]:
      output.append(array1[0])
      array1.pop(0)
    else:
      output.append(array2[0])
      array2.pop(0)

  if array1:        #append the remaining items from the longest array as they are already sorted
    for e in array1:
      output.append(e)
  else:
    for e in array2:
      output.append(e)
  
  return output

print(mergeSortedArray([1,3,5,6],[5,6,7,10,15]))

#Time complexity - O(n^2) because of pop(index)
#Space complexity - O(1)
    
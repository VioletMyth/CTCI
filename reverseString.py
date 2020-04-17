def reverseString(string):
  if (type(string) != str):   #checks if param is of string type
    return "Not of string type"
  elif len(string) == 0:      #checks if string is emppty
    return "Empty string"
  outString = ""
  for i in range(len(string)-1,-1,-1):  #run for loop backwards and append to outString
    outString += string[i]
  return outString

def reverseString2(string): #does same for less increased readability
  outString = list(string)
  outString.reverse()
  return ''.join(outString)
  
print(reverseString("12312312312"))
print(reverseString2("12312312312"))
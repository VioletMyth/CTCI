def stringCompression(string):
    stack = []
    outString = ""
    i = 0
    sList = list(string)
    while i < len(sList):
        if len(stack) == 0 or sList[i] in stack:
            stack.append(sList[i])
        else:
            outString = outString + stack[-1] + str(len(stack))
            stack.clear()
            stack.append(sList[i])
        
        i += 1
    outString = outString + stack[-1] + str(len(stack))
    
    if len(outString) > len(string):
        return string
    else:
        return outString

def stringCompression2(string):
    prevChar = None
    outString = ""
    counter = 0
    for char in string:
        if prevChar == None or prevChar == char:
            counter += 1
        else:
            outString = outString + prevChar + str(counter)
            counter = 1 
        prevChar = char
    outString = outString + char + str(counter)

    if len(outString) > len(string):
        return string
    else:
        return outString
print(stringCompression2("Hello world"))

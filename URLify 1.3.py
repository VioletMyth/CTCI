def replaceString1(inputString, length):
    stringList = list(inputString)
    print(stringList)
    i = length - 1
    index = len(inputString)-1
    while i >= 0:
        if stringList[i] != " ":
            stringList[index-1] = stringList[i]
            index-=1
        else:
            stringList[index - 1] = "0"
            stringList[index - 2] = "2"
            stringList[index - 3] = "%"
            index-=3
        
    return stringList

def replaceString2(inputString, length):
    outputString = ""
    i = 0
    while i < length:
        if inputString[i] == " ":
            outputString += "%20"
        else:
            outputString += inputString[i]

        i+=1
    return outputString

print(replaceString1("Mr John Smith    ", 13))
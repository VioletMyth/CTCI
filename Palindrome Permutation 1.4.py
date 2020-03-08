def palindromePermutation(s):
    sList = list(s.replace(" ", "").lower())
    print(sList)
    sList = sorted(sList)
    hashmap = {}
    for char in sList:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1
    
    if len(sList) % 2 == 0:
        isEven = True
    else:
        isEven = False
    
    if isEven:
        for key in hashmap:
            if key != " " and hashmap[key] % 2 != 0:
                print("we are here")
                return False
    
    else:
        alreadyOdd = 0
        for key in hashmap:
            if key != " ":
                if hashmap[key] % 2 == 1:
                    alreadyOdd +=1
        if alreadyOdd > 1:
            return False
    
    return True

print(palindromePermutation("ATATATATATATAATATATATT"))
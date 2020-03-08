def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    hashmap1 = {}
    hashmap2 = {}

    for character in string1:
        if character not in hashmap1:
            hashmap1[character] = 1
        
        else:
            hashmap1[character] += 1
        
    for char in string2:
        if char not in hashmap2:
            hashmap2[char] = 1
        
        else:
            hashmap2[char] += 1
    
    for key in hashmap1:
        if key not in hashmap2:
            return False
        if hashmap1[key] != hashmap2[key]:
            return False
        

    return True

print(isPermutation("your mum is gayasd", "your mum is gay"))
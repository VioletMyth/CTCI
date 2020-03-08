def oneAway(string1, string2):
    if string1 == string2:
        return True
    if len(string1) == len(string2):
        k = len(string1)
    
    else:
        k = max(len(string1), len(string2))
    
    i = 0
    j = 0
    counter = 0

    while i < k:
        if string1[i] == string2[j]:
            j += 1
        else:
            if counter == 0:
                counter += 1
            else:
                return False
        i += 1

    return True

print(oneAway("pale", "bake"))
print(oneAway("penis", "lobster"))
print(oneAway("bake ", "bake"))
def mergeStringsAlternately(w1, w2):
    merged = ""
    i, j = 0, 0

    while i < len(w1) and j < len(w2):
        merged += w1[i] + w2[j]
        i += 1
        j += 1
    
    merged += w1[i:] + w2[j:]

    return merged

print(mergeStringsAlternately("abc", "pqr"))
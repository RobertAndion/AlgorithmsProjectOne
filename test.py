
def checkSorted(collection) -> bool: # Function to assert whether an array is properly sorted.
    if len(collection) < 2:
        return True
    highest = collection[0]
    for i in range (1,len(collection)):
        if collection[i] == highest:
            continue
        if collection[i] < highest:
            return False
        if collection[i] > highest:
            highest = collection[i]
    return True

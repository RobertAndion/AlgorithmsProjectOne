
def insertionsort(collection):
    for i in range(1,len(collection)): # Iterate whole collection
        for j in range(0,i): # Iterate distance i to 0
            if collection[i - j] < collection[i - j - 1]: # If the one before is greater than current swap
                temp = collection[i - j]            # do the swap
                collection[i - j] = collection[i - j - 1]
                collection[i - j - 1] = temp
    return collection

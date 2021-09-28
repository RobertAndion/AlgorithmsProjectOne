def selectionsort(collection):
    for i in range(0,len(collection)): # Main loop
        min = i
        for j in range(i+1,len(collection)): # Loop from i to n
            if collection[j] < collection[min]:
                min = j                      # Find min
        temp = collection[min]               # Swap collection i with min
        collection[min] = collection[i]
        collection[i] = temp
    
    return collection
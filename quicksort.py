import math
import statistics

def quicksort(collection, start, stop) -> None: # Needs to handle the constant data case, pivot never moves and it fails. Works for less than 1000.
    if (stop - start) <= 1:
        return

    if stop - start > 3: # Else just use index 0 since we need at least 3 elements for median of three
        medianOfThreeCollection = []
        medianOfThreeCollection.append(collection[start])
        medianOfThreeCollection.append(collection[stop - 1])
        medianOfThreeCollection.append(collection[math.floor((stop - start - 1)/ 2)])
        median = statistics.median(medianOfThreeCollection)
        pivotIndex = -1
        if collection[start] == median:
            pivotIndex = start
        elif collection[math.floor((stop - start - 1) / 2)] == median:
            pivotIndex = math.floor((stop - start - 1) / 2)
        else:
            pivotIndex = stop - 1
        # We now have the correct pivot from median of three.
        temp = collection[start]
        collection[start] = collection[pivotIndex] # swap median to index zero for sorting reasons
        collection[pivotIndex] = temp

    pivotIndex = start
    for i in range(start + 1,stop):
        if collection[i] < collection[pivotIndex]:
            temp = collection[pivotIndex] # Store current pivot
            collection[pivotIndex] = collection[i] # Swap less value with pivot
            pivotIndex += 1
            collection[i] = collection[pivotIndex] #Swap value after pivot with old i value
            collection[pivotIndex] = temp # Move the pivot forward one

    quicksort(collection, start, pivotIndex)
    quicksort(collection, pivotIndex + 1, stop)


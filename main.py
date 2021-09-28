import sys
import time
import generateArrays as makeArrays
import selectionsort
import insertionsort
import quicksort
import test
def main():
    if len(sys.argv) != 4:
        print("Please enter the correct arguments.")
    else:
        arrayToSort = ''
        try:
            if sys.argv[3] == 's':
                arrayToSort = makeArrays.generateSortedArray(int(sys.argv[2]))
            elif sys.argv[3] == 'c':
                arrayToSort = makeArrays.generateZeroArray(int(sys.argv[2]))
            elif sys.argv[3] == 'r':
                arrayToSort = makeArrays.generateRandomArray(int(sys.argv[2]))
            else:
                print("Please select a valid array format (s,c,r)")
                return -1
        except:
            print("Please enter a valid number.")
            return -1

        if sys.argv[1] == 'q':
            start = time.time()
            print('Start: ' + str(start))
            try:
                quicksort.quicksort(arrayToSort, 0, len(arrayToSort))
            except:
                print("Quick sort overloaded the stack python provides and failed. (1000 stack limit)")
                return -1
            stop = time.time()
            print('Stop: ' + str(stop))
            print('Runtime: ' + str(stop - start))
            if test.checkSorted(arrayToSort):
                print('Data correctly sorted after running Quick Sort.')
            else:
                print('Data incorrectly sorted after running Quick Sort')
        elif sys.argv[1] == 'i':
            start = time.time()
            print('Start: ' + str(start))
            arrayToSort = insertionsort.insertionsort(arrayToSort)
            stop = time.time()
            print('Stop: ' + str(stop))
            print('Runtime: ' + str(stop - start))
            if test.checkSorted(arrayToSort):
                print('Data correctly sorted after running Insertion Sort.')
            else:
                print('Data incorrectly sorted after running Insertion Sort')

        elif sys.argv[1] == 's':
            start = time.time()
            print('Start: ' + str(start))
            arrayToSort = selectionsort.selectionsort(arrayToSort)
            stop = time.time()
            print('Stop: ' + str(stop))
            print('Runtime: ' + str(stop - start))
            if test.checkSorted(arrayToSort):
                print('Data correctly sorted after running Selection Sort.')
            else:
                print('Data incorrectly sorted after running Selection Sort')
        else:
            print("Please select a valid algorithm (q,i,s)")
            return -1


if __name__ == "__main__":
    main()
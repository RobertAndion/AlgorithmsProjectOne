import random
import sys

def generateZeroArray(length):
    return [0] * length

def generateSortedArray(length):
    ret = []
    for i in range(0,length):
        ret.append(i)
    return ret

def generateRandomArray(length): # Ask if we want obscurely large numbers or add % something to bound it
    ret = []
    for i in range(0,length):
        ret.append(random.randint(0,sys.maxsize) % 100)
    return ret
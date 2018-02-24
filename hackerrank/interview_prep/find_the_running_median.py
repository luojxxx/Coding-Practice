# https://www.hackerrank.com/challenges/ctci-find-the-running-median
import math
class RunningMedian:
    def __init__(self):
        #minheap
        self.minHeap = []
        self.maxHeap = []

    def parent(self, idx):
        parentIdx = math.floor((idx-1)/2.0)
        if parentIdx < 0:
            return None
        else:
            return parentIdx

    def leftChild(self, idx, heapSize):
        childIdx = (2*idx) + 1
        if childIdx >= heapSize:
            return None
        else:
            return childIdx

    def rightChild(self, idx, heapSize):
        childIdx = (2*idx) + 2
        if childIdx >= heapSize:
            return None
        else:
            return childIdx

    def minHeapCheck(self):
        heapSize = len(self.minHeap)
        lastIdx = heapSize - 1
        def swapUp(currentIdx):
            parentIdx = self.parent(currentIdx)
            if parentIdx == None:
                return
            if self.minHeap[currentIdx] < self.minHeap[parentIdx]:
                self.minHeap[currentIdx], self.minHeap[parentIdx] = self.minHeap[parentIdx], self.minHeap[currentIdx] 
                swapUp(parentIdx)
        swapUp(lastIdx)

    def maxHeapCheck(self):
        heapSize = len(self.maxHeap)
        lastIdx = heapSize - 1
        def swapUp(currentIdx):
            parentIdx = self.parent(currentIdx)
            if parentIdx == None:
                return
            if self.maxHeap[currentIdx] > self.maxHeap[parentIdx]:
                self.maxHeap[currentIdx], self.maxHeap[parentIdx] = self.maxHeap[parentIdx], self.maxHeap[currentIdx] 
                swapUp(parentIdx)
        swapUp(lastIdx)

    def provideMedian(self):
        minHeapSize = len(self.minHeap)
        maxHeapSize = len(self.maxHeap)
        if minHeapSize==0 and maxHeapSize==0:
            return None

        if minHeapSize > maxHeapSize:
            return float(self.minHeap[0])
        elif minHeapSize < maxHeapSize:
            return float(self.maxHeap[0])

        if minHeapSize == maxHeapSize:
            return (self.minHeap[0]+self.maxHeap[0])/2

    def add(self, val):
        # print('adding val', val)
        heapDiff = len(self.minHeap) - len(self.maxHeap)
        if self.provideMedian() == None:
            self.minHeap.append(val)
            print(self.provideMedian())
            return self.provideMedian()

        if val > self.provideMedian():
            self.minHeap.append(val)
        elif val < self.provideMedian():
            self.maxHeap.append(val)
        elif val == self.provideMedian():
            if heapDiff > 0:
                self.maxHeap.append(val)
            else:
                self.minHeap.append(val)
        else:
            self.maxHeap.append(val)
        # print(self.minHeap)
        # print(self.maxHeap)
        
        # print('diff is', heapDiff)
        heapDiff = len(self.minHeap) - len(self.maxHeap)
        if heapDiff >= 2:
            self.maxHeap.append(self.minHeap.pop(0))
        if heapDiff <= -2:
            self.minHeap.append(self.maxHeap.pop(0))

        self.minHeapCheck()
        self.maxHeapCheck()

        # print(self.minHeap)
        # print(self.maxHeap)
        # print(self.minHeap[0], self.maxHeap[0])
        print(self.provideMedian())
        
        return self.provideMedian()

import statistics

test = RunningMedian()
slist = [94455, 20555, 20535, 53125, 73634, 148]
slist = [1,2,3,4,5,6,7,8,9,10]
slist = [float(i) for i in open('/Users/cloudlife/Desktop/input01.txt').readlines()]
import numpy as np
# slist = [np.random.randint(1,99) for i in range(7)]
for val in slist:
    test.add(val)
statistics.median(slist)
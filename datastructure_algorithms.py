import os
folderpath = '/Users/cloudlife/Desktop/'
def openFile(fileName):
    return open( fileName, 'r').read().split()

def openFile(fileName):
    data = []
    for row in open(fileName, 'r'):
        data.append(row.strip().split(' '))
    return data

def checkAgainstTest(customFn, inputFile, outputFile):
    dataIn = openFile(inputFile)
    dataOut = openFile(outputFile)
    dataIn.pop(0)
    results = [ customFn(float(linein)) == float(lineout) for linein, lineout in zip(dataIn, dataOut) ]
    return results, dataIn, dataOut

def gatherNodes(node):
    if node.left != None and node.right != None:
        return gatherNodes(node.left) + gatherNodes(node.right) + [node.data]
    if node.left != None and node.right == None:
        return gatherNodes(node.left ) + [node.data]
    if node.left == None and node.right != None:
        return gatherNodes(node.right) + [node.data]
    if node.left == None and node.right == None:
        return [node.data]


# https://www.hackerrank.com/challenges/ctci-making-anagrams
from collections import Counter
def number_needed(a, b):
    aCounts = Counter(a)
    bCounts = Counter(b)

    aSet = set(aCounts)
    bSet = set(bCounts)

    similar = aSet.intersection(bSet)
    differences = aSet.symmetric_difference(bSet)

    matchingKeysDiff = sum([ abs(aCounts[key] - bCounts[key]) for key in similar ])

    differentKeysDiff = 0
    for key in differences:
        if key in aCounts:
            differentKeysDiff += aCounts[key]
        if key in bCounts:
            differentKeysDiff += bCounts[key]

    return matchingKeysDiff + differentKeysDiff

# https://www.hackerrank.com/challenges/ctci-ransom-note
from collections import Counter
def ransom_note(magazine, ransom):
    ransomCount = Counter(ransom)
    magazineCount = Counter(magazine)

    ransomSet = set(ransomCount)
    magazineSet = set(magazineCount)

    if not ransomSet.issubset(magazineSet):
        return False

    matchingWords = ransomSet.intersection(magazineSet)

    for word in matchingWords:
        if ransomCount[word] > magazineCount[word]:
            return False

    return True

# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
def has_cycle(head):
    visitHistory = []
    visitHistory.append(head.data)
    nextNode = head.next
    while nextNode != None:
        if nextNode.data in visitHistory:
            return True
        visitHistory.append(nextNode.data)
        nextNode = nextNode.next
    return False

# https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    matching = {'}':'{', ']':'[', ')':'('}
    stack = []
    for char in expression:
        if char in ['[', '{', '(']:
            stack.append(char)
        if char in [']', '}', ')']:
            if len(stack) == 0:
                return False
            if matching[char] != stack.pop():
                return False
    if len(stack) == 0:
        return True
    else:
        return False

# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.stackNew = []
        self.stackOld = []

    def put(self, value):
        self.stackNew.append(value)

    def pop(self):
        self.check()
        self.stackOld.pop()

    def peek(self):
        self.check()
        return self.stackOld[-1]

    def check(self):
        if len(self.stackOld) == 0:
            self.stackNew.reverse()
            self.stackOld = self.stackNew
            self.stackNew = []

# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check(node, depth = 0):
    if node.left != None and node.right != None:
        stateLeft, valMinLeft, valMaxLeft = check(node.left )
        stateRight, valMinRight, valMaxRight = check(node.right )
        newState = None
        if stateLeft == False or stateRight == False:
            newState = False
        elif valMaxLeft < node.data and valMinRight > node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMinLeft, valMinRight, node.data), max(valMaxLeft, valMaxRight, node.data)]

    if node.left != None and node.right == None:
        state, valMin, valMax = check(node.left)
        newState = None
        if state == False:
            newState = False
        elif valMax < node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMin, node.data), max(valMax, node.data)]

    if node.left == None and node.right != None:
        state, valMin, valMax = check(node.right)
        newState = None
        if state == False:
            newState = False
        elif valMin > node.data:
            newState = True
        else:
            newState = False
        return [newState, min(valMin, node.data), max(valMax, node.data)]

    if node.left == None and node.right == None:
        return [True, node.data, node.data]

def check_binary_search_tree_(root):
    #optimal finds the min, max at each node
    state, _, _  = check(root)
    return state

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

# https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/
class trieNode:
    __slots__ = ['count', 'char', 'childrenDic']
    def __init__(self, char, childrenDic, countInit = 1):
        self.count = countInit
        self.char = char
        self.childrenDic = {}
    def iterateCounter(self):
        self.count += 1
    def addChild(self, char):
        if char not in self.childrenDic:
            childNode = trieNode(char, {})
            self.childrenDic[char] = childNode
            return childNode
        else:
            self.childrenDic[char].iterateCounter()
            return self.childrenDic[char]

def addContact(rootNode, name):
    currentNode = rootNode
    for idx in range(0, len(name) -1):
        char = name[idx]
        nextChar = name[idx+1]
        currentNode = currentNode.addChild(nextChar)

    return rootNode

def findContact(rootNode, name):
    try:
        currentNode = rootNode
        for idx in range(0, len(name) -1):
            char = name[idx]
            nextChar = name[idx+1]
            currentNode = currentNode.childrenDic[nextChar]

        return currentNode.count

    except:
        return 0

contactGraph = trieNode(' ', {}, 0)
def runTrieContacts(op, contact):
    contact = ' '+contact
    if op == 'add':
        addContact(contactGraph, contact)
    if op == 'find':
        print(findContact(contactGraph, contact))

# https://www.hackerrank.com/challenges/ctci-bubble-sort
def bubblesort(arr):
    totalSwaps = 0
    runSwap = 1
    while runSwap != 0:
        
        runSwap = 0
        for idx in range(0,len(arr)-1):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                runSwap +=1

        totalSwaps += runSwap

    print('Array is sorted in %s swaps.' % totalSwaps)
    print('First Element: %s' % arr[0])
    print('Last Element: %s' % arr[-1])

# https://www.hackerrank.com/challenges/ctci-comparator-sorting
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name + ' ' + self.score
        
    def comparator(a, b):
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.name == b.name:
                return 0
            if [a.name, b.name] == sorted([a.name, b.name]):
                return -1
            else:
                return 1

# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
def iceCreamBuys(money, prices):
    prices = [int(i) for i in prices]
    if prices.count(money/2) >= 2:
        indices = [idx for idx,val in enumerate(prices) if val == money/2]
        return str(indices[0]+1) +' '+ str(indices[1]+1)
    setPrices = set(prices)
    for split1 in range(1, money):
        split2 = money - split1
        # print(split1, split2)
        if split1 in setPrices and split2 in setPrices:
            indices = [prices.index(split1), prices.index(split2)]
            indices.sort()
            return str(indices[0]+1) +' '+ str(indices[1]+1)

def findRoot(num, precision):
    num = float(num)
    def binarySearch(num, precision, low, high):
        mid = low+((high-low)/2)
        midSquared = mid**2
        # print(num, precision, low, mid, high)
        if abs(midSquared-num) < precision or midSquared==num:
            return mid
        if midSquared < num:
            return binarySearch(num, precision, mid, high)
        if midSquared > num:
            return binarySearch(num, precision, low, mid)

    return binarySearch(num, precision, 0.0, num)

# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
def findValidNodes(grid):
    validNodeArr = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                validNodeArr.append((i, j))
    return validNodeArr

def adjacentValidNodes(grid, position):
    gridSize_i = len(grid)
    gridSize_j = len(grid[0])
    i = position[0]
    j = position[1]

    adjacentSet = {
    (i-1, j-1),
    (i-1, j+1),
    (i+1, j-1),
    (i+1, j+1),
    (i-1, j),
    (i+1, j),
    (i, j-1),
    (i, j+1)
    }

    validAdjacent = set([])
    for adjacentCoor in adjacentSet:
        if (0 <= adjacentCoor[0] < gridSize_i) and (0 <= adjacentCoor[1] < gridSize_j):
            if grid[adjacentCoor[0]][adjacentCoor[1]] == 1:
                validAdjacent.add(adjacentCoor)

    return validAdjacent

def trip(grid, start):
    visited = set([start])
    stack = list(adjacentValidNodes(grid, start))

    while len(stack) != 0:
        goToCoor = stack.pop()
        visited.add(goToCoor)
        newAdajcentCoor = [coor for coor in adjacentValidNodes(grid, goToCoor)
        if coor not in stack and coor not in visited]
        stack += newAdajcentCoor

    return visited

grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
def getBiggestRegion(grid):
    allValidNodes = set(findValidNodes(grid))
    trips = []

    while len(allValidNodes) != 0:
        start = allValidNodes.pop()
        visited = trip(grid, start)
        trips.append(len(visited))
        allValidNodes = allValidNodes.difference(visited)

    return max(trips)

# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
import queue
class Graph:
    def __init__(self, n):
        self.dic = {i:[] for i in range(0,n)}

    def connect(self, a, b):
        self.dic[a].append(b)
        self.dic[b].append(a)

    def find_all_distances(self, start):
        visited = [-1 for i in range(len(self.dic))]
        visited[start] = 0
        unvisited = set(list(range(len(self.dic))))
        q = queue.Queue()
        q.put(start)

        while not q.empty():
            currentNode = q.get_nowait()

            distance = visited[currentNode] + 6
            for neighbor in self.dic[currentNode]:
                if neighbor in unvisited:
                    q.put(neighbor)
                    visited[neighbor] = distance
                    unvisited.remove(neighbor)

        del visited[start]

        printStr = ''
        for distance in visited:
            printStr += str(distance) + ' '
        print(printStr)

# https://www.hackerrank.com/challenges/ctci-big-o
def primeBool(num):
    if num in [0, 1]:
        return 'Not prime'

    sqrt = int(num**0.5)
    for i in range(2, sqrt+1):
        if num % i == 0:
            return 'Not prime'
    return 'Prime'

# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
def fibonacci(n):
    fibDic = {0:0, 1:1}
    def fib(n):
        if n in fibDic:
            return fibDic[n]
        else:
            answer = fib(n-1)+fib(n-2)
            fibDic[n] = answer
            return answer
    return fib(n)

# https://www.hackerrank.com/challenges/ctci-recursive-staircase
import math
import functools
def multipleObjectPermutation(arr):
    dividend = math.factorial(sum(arr))
    divisor = [math.factorial(ele) for ele in arr]
    divisor = functools.reduce(lambda x, y: x*y, divisor)
    return int(dividend/divisor)

def counterRawCounts(counter):
    return [counter[key] for key in counter]

from collections import Counter
import itertools
import time
def davisStaircase(val):
    if val == 1:
        return 1
    elif val == 2:
        return 2
    # time1 = time.time()
    oneArr = [1 for i in range(val)]

    combos = set([tuple(oneArr)])
    def combine(oldArray, jump):
        arr = oldArray[:]
        arr.reverse()
        # print(arr, jump)

        if jump == 'a':
            arr.pop()
            arr.pop()
            arr.append(2)
        if jump == 'b':
            arr.pop()
            arr.pop()
            arr.pop()
            arr.append(3)
        if jump == 'c':
            arr.pop()
            arr.remove(2)
            arr.append(3)

        arr.sort()
        combos.add(tuple(arr))
        onesCount = arr.count(1)
        twosCount = arr.count(2)
        if onesCount >= 2:
            combine(arr, 'a')
        if onesCount >= 3:
            combine(arr, 'b')
        if onesCount >= 1 and twosCount >= 1:
            combine(arr, 'c')

    combine(oneArr, 'a')
    combine(oneArr, 'b')
    # combine(oneArr, 'c')
    
    # time2 = time.time()
    # print(combos)
    uniqueCounts = [multipleObjectPermutation(counterRawCounts(Counter(combo))) for combo in combos]
    # time3 = time.time()
    # print(time2 - time1)
    # print(time3 - time2)
    return sum(uniqueCounts)

def davisStaircase(n):
    memo = {1:1, 2:2, 3:4}
    def recurse(n):
        if n in memo:
            return memo[n]
        else:
            answer = recurse(n-1)+recurse(n-2)+recurse(n-3)
            memo[n] = answer
            return answer
    return recurse(n)

# https://www.hackerrank.com/challenges/ctci-coin-change
def make_change(coins, n):
    coins.sort()
    coins = [i for i in coins if i <= n]
    memo = {}

    def breakdown(coins, val):
        if val in memo:
            return memo[val]
        if val < coins[0]:
            return None

        validCombos = set([])
        if val in coins:
            validCombos.add(tuple([val]))
        for coin in coins:
            combos = breakdown(coins, val - coin)
            # print(val, coin, val-coin,  combos)
            if combos != None:
                for combo in combos:
                    validCombos.add(tuple(sorted([coin]+combo)))

        validCombos = [list(arr) for arr in validCombos]
        memo[val] = validCombos
        return validCombos

    return breakdown(coins, n)

def make_change(coins, n):
    memo = [0 for i in range(n+1)]
    memo[0] = 1
    for coin in coins:
        for value in range(n+1):
            if value >= coin:
                memo[value] += memo[value-coin]

    return memo[-1]

# https://www.hackerrank.com/challenges/ctci-lonely-integer
def lonely_integer(a):
    bitArray = 0b0
    for ele in a:
        bitArray = bitArray ^  ele
        # print(ele, bin(bitArray))

    return int(bitArray)

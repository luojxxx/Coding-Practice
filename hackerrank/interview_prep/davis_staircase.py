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
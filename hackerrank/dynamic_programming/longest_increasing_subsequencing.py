# Longest Increasing subsequence https://www.hackerrank.com/challenges/longest-increasing-subsequent
def lisWithEnd(arr):
    if len(arr) == 0:
        return []

    upperBound = arr.pop()
    arr.reverse()
    newArr = [upperBound]
    for val in arr:
        if val <= upperBound:
            newArr.append(val)
            # upperBound = val
    newArr.reverse()
    return newArr

assert lisWithEnd([1,2,3]) == [1,2,3]
assert lisWithEnd([1,5,9,6]) == [1,5,6]
assert lisWithEnd([1]) == [1]
assert lisWithEnd([]) == []

def lis(arr):
    memo = { }

    for idx in range(0, len(arr)):
        subArr = arr[0:idx+1]
        memo[idx+1] = lisWithEnd(subArr)

    return max([ len(memo[key]) for key in memo])
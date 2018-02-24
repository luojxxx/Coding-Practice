# https://www.hackerrank.com/challenges/mandragora
def genSums(arr):
    memo = {}
    total = 0
    for idx , val in reversed(list(enumerate(arr))):
        total += val
        memo[idx+1] = total
    return memo

def splitEatBattle(strength, memo):
    # strength = idx + 1
    return strength*memo[strength]

def maxXp(arr):
    arr = [int(val) for val in arr.split(' ')]
    arr.sort()

    memo = genSums(arr)
    xpArr =[]
    for idx in range(1, len(arr)+1):
        xpArr.append(splitEatBattle(idx, memo))
    return max(xpArr)
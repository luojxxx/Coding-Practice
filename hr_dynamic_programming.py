# Enter your code here. Read input from STDIN. Print output to STDOUT
# numTest = input()

# def distribute(numPpl, distro):
#     return 1

# for _ in range(int(numTest)):
#     numPpl = input()
#     distro = input()
#     print(distribute(numPpl, distro))

#Coin change https://www.hackerrank.com/challenges/coin-change
def makeChange(val, coins):
    memo = {}

    def breakdown(val, coins):
        if val in memo:
            return memo[val]
        elif val ==0:
            return 1
        elif val < 0:
            return 0

        total = sum([breakdown(val - coin, coins) for coin in coins])
        memo[val] = total
        return total

    grandTotal = breakdown(val, coins)
    print(memo)
    return grandTotal


def makeChange(val, coins):
    memo=[0 for i in range(val+1)]
    memo[0] = 1

    for coin in coins:
        for currentVal in range(len(memo)):
            if currentVal >=coin:
                memo[currentVal] += memo[currentVal-coin]

    return memo[val]

# Equal https://www.hackerrank.com/challenges/equal
def subChoco(idx, val, distro):
    distro[idx] -= val
    return distro

def minMax(arr):
    minVal = 9999999999
    maxVal = 0
    maxIdx = 0
    for idx, val in enumerate(arr):
        if val < minVal:
            minVal = val
        if val > maxVal:
            maxVal = val
            maxIdx = idx
    return minVal, maxVal, maxIdx

def equalize(distro):
    # minVal = min(distro)
    # maxVal = max(distro)
    # maxIdx = distro.index(maxVal)
    minVal, maxVal, maxIdx = minMax(distro)
    diff = maxVal - minVal

    if diff >= 5:
        # print(5,distro)
        return subChoco(maxIdx, 5, distro)
    if diff >= 2:
        # print(2,distro)
        return subChoco(maxIdx, 2, distro)
    if diff >= 1:
        # print(1,distro)
        return subChoco(maxIdx, 1, distro)

def distribute(distro):
    distro = [int(ele) for ele in distro.split(' ')]

    if len(set(distro)) == 1:
        return 0

    count = 0
    while len(set(distro)) > 1:
        distro = equalize(distro)
        count += 1

    return count



# Longest Increasing subsequence https://www.hackerrank.com/challenges/longest-increasing-subsequent
# length = int(input())

# arr = []
# for _ in range(length):
#     arr.append(int(input()))

# def lis(arr):
#     memo={0: arr[0]}
    
#     for idx in range(1,len(arr)):
#         seq = memo[idx]

#         if seq[-1] > arr[idx]:
#             


def output(digits, idx, arr):
    convert = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6: 'mno', 7:'pqrs', 8: 'tuv', 9:'wxyz', 0:''}
    newDigits = digits[:]
    if all([type(ele) is str for ele in newDigits]):
        arr.append(newDigits)
        return 

    num = newDigits[idx]
    if type(num) is int:
        for char in list(convert[num]):
            newDigits[idx] = char
            output(newDigits, idx+1, arr)

def numToWords(digits):
    digits = [int(ele) for ele in list(digits)]
    memo = []
    output(digits, 0, memo)
    return [ele[0]+ele[1] for ele in memo]
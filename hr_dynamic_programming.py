# # Enter your code here. Read input from STDIN. Print output to STDOUT
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
memo = {1:1, 2:1, 3:2, 4:2, 5:1}
def minOps(val, counter, memo):
    # print(val, counter, memo)
    if val in memo:
        return memo[val]
    elif val==0:
        return counter
    elif val<0:
        return 99999999999999
    else:
        arr = [
            minOps(val-1, counter+1, memo)+1,
            minOps(val-2, counter+1, memo)+1,
            minOps(val-5, counter+1, memo)+1]
        # print(arr)
        memo[val] = min(arr)
        return memo[val]

def distribute(distro, memo):
    distro = [int(ele) for ele in distro.split(' ')]
    if len(set(distro)) == 1:
        return 0

    totals = []
    distro = [ele+10 for ele in distro] #because the optimal answer might be negative ex [-1,-1,-1]
    distroMin = min(distro)
    distroMinLowerBound = distroMin-5 if distroMin-5>0 else 0 #limit range of values to check
    for minVal in range(distroMinLowerBound, distroMin+1):
        distroCopy = distro[:]
        distroCopy = [val - minVal for val in distroCopy]
        count = sum([minOps(val, 0, memo) for val in distroCopy])
        totals.append(count)

    return min(totals)

def fileImport(name):
    return [i.strip('\n') for i in open('/Users/cloudlife/Desktop/%s.txt' % name).readlines()]

def comparator(dataInName, dataInSpacing, dataOutName, dataOutSpacing):
    dataIn = fileImport(dataInName)
    dataOut = fileImport(dataOutName)

    dataInLength = dataIn.pop(0) #gets the number of test cases
    dataIn = [ (dataIn[i], dataIn[i+1]) for i in range(0, len(dataIn), dataInSpacing) ] #groups testcase info

    errorCount = 0
    for i in range(0, len(dataIn)):
        testcase = dataIn[i][1]
        testcaseAns = dataOut[i]

        funcOutput = distribute(testcase, memo)
        err = ''
        if int(funcOutput) != int(testcaseAns):
            err = 'mismatch'
            errorCount+=1
        print(testcaseAns, funcOutput, err)
    print(errorCount)


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


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
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
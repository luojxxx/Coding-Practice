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
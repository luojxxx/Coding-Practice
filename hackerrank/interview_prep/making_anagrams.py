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
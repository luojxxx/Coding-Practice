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
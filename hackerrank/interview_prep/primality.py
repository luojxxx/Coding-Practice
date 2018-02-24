# https://www.hackerrank.com/challenges/ctci-big-o
def primeBool(num):
    if num in [0, 1]:
        return 'Not prime'

    sqrt = int(num**0.5)
    for i in range(2, sqrt+1):
        if num % i == 0:
            return 'Not prime'
    return 'Prime'
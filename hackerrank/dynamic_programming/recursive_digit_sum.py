# https://www.hackerrank.com/challenges/recursive-digit-sum
def super_digit(n, k):
    def _compute(num):
        num_str = str(num)
        total = sum(map(int, num_str))
        if len(str(total)) == 1:
            return total
        else:
            return _compute(total)
        
    # n, k = [int(x) for x in raw_input().strip().split()]
    concat = int(str(n) * k)
    if len(str(concat)) == 1:
        return concat
    else:
        return _compute(concat)
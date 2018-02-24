# https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
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
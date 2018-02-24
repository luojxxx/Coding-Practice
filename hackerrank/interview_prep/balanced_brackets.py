# https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    matching = {'}':'{', ']':'[', ')':'('}
    stack = []
    for char in expression:
        if char in ['[', '{', '(']:
            stack.append(char)
        if char in [']', '}', ')']:
            if len(stack) == 0:
                return False
            if matching[char] != stack.pop():
                return False
    if len(stack) == 0:
        return True
    else:
        return False
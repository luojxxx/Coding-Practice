# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
def fibonacci(n):
    fibDic = {0:0, 1:1}
    def fib(n):
        if n in fibDic:
            return fibDic[n]
        else:
            answer = fib(n-1)+fib(n-2)
            fibDic[n] = answer
            return answer
    return fib(n)
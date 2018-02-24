# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class MyQueue(object):
    def __init__(self):
        self.stackNew = []
        self.stackOld = []

    def put(self, value):
        self.stackNew.append(value)

    def pop(self):
        self.check()
        self.stackOld.pop()

    def peek(self):
        self.check()
        return self.stackOld[-1]

    def check(self):
        if len(self.stackOld) == 0:
            self.stackNew.reverse()
            self.stackOld = self.stackNew
            self.stackNew = []
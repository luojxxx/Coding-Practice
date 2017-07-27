#######
class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

#######
class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

#######
class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

#######
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

#######
def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

# main()

################################################################################
################################################################################
################################################################################
################################################################################
# Helper library pulled from Peter Norvig's answers to learn from
# since he found these functions particularly helpful

import re
import numpy as np
import math
import urllib.request

from collections import Counter, defaultdict, namedtuple, deque
from functools   import lru_cache
from itertools   import permutations, combinations, chain, cycle, product, islice
from heapq       import heappop, heappush

def fileImport(name):
    return [i.strip('\n') for i in open('/Users/cloudlife/Desktop/%s.txt' % name).readlines()]

def Input(day):
    "Open this day's input file."
    filename = 'advent2016/input{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        return urllib.request.urlopen("http://norvig.com/ipython/" + filename)

def mapCombine(func, array):
    return list(chain.from_iterable([func(ele) for ele in array]))

def transpose(matrix): return zip(*matrix)

def first(iterable): return next(iter(iterable))

def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)

cat = ''.join

Ø   = frozenset() # Empty set
inf = float('inf')
BIG = 10 ** 999

def grep(pattern, lines):
    "Print lines that match pattern."
    for line in lines:
        if re.search(pattern, line):
            print(line)

def groupby(iterable, key=lambda it: it):
    "Return a dic whose keys are key(it) and whose values are all the elements of iterable with that key."
    dic = defaultdict(list)
    for it in iterable:
        dic[key(it)].append(it)
    return dic

def powerset(iterable):
    "Yield all subsets of items."
    items = list(iterable)
    for r in range(len(items)+1):
        for c in combinations(items, r):
            yield c

# 2-D points implemented using (x, y) tuples
def X(point): return point[0]
def Y(point): return point[1]

def neighbors4(point): 
    "The four neighbors (without diagonals)."
    x, y = point
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

def neighbors8(point): 
    "The eight neighbors (with diagonals)."
    x, y = point 
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (X+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def cityblock_distance(p, q=(0, 0)): 
    "City block distance between two points."
    return abs(X(p) - X(q)) + abs(Y(p) - Y(q))

def euclidean_distance(p, q=(0, 0)): 
    "Euclidean (hypotenuse) distance between two points."
    return math.hypot(X(p) - X(q), Y(p) - Y(q))

def trace1(f):
    "Print a trace of the input and output of a function on one line."
    def traced_f(*args):
        result = f(*args)
        print('{}({}) = {}'.format(f.__name__, ', '.join(map(str, args)), result))
        return result
    return traced_f

def astar_search(start, h_func, moves_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
    frontier  = [(h_func(start), start)] # A priority queue, ordered by path length, f = g + h
    previous  = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}     # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))
                
def Path(previous, s): 
    "Return a list of states that lead to state s, according to the previous dict."
    return ([] if (s is None) else Path(previous, previous[s]) + [s])


################################################################################
################################################################################
################################################################################
################################################################################




#DAY 4 Security through obscurity
file = [i.strip('\n') for i in open('/Users/cloudlife/Desktop/input4.txt').readlines()]

def checkSummer(counts):
    checkSumList = []
    temp = ''
    priorNum = counts[0][1]
    for ele in counts:
        char = ele[0]
        num = ele[1]

        if priorNum == num:
            temp += char

        if priorNum != num:
            checkSumList.append(''.join(sorted(temp)))
            temp = ''
            priorNum = num
            temp+=char

    checkSumList.append(''.join(sorted(temp)))

    return ''.join(checkSumList)[0:5]

def checkRoomName(name):
    matches = re.match( r'([a-z\-]+)(\d+)(\[.+\])', name)

    dashedName = matches.group(1)
    encryptName = dashedName.replace('-', '')
    sectorId = int(matches.group(2))
    checkSum = matches.group(3)[1:-1]

    nameCounts = collections.Counter(encryptName).most_common()
    nameCheckSum = checkSummer(nameCounts)
    if checkSum == nameCheckSum:
        return dashedName, sectorId
    else:
        return '', 0

# assert checkRoomName('aaaaa-bbb-z-y-x-123[abxyz]') == 123
# assert checkRoomName('a-b-c-d-e-f-g-h-987[abcde]') == 987
# assert checkRoomName('not-a-real-room-404[oarel]') == 404

# total = 0
# realRooms = []
# for room in file:
#     dashedName, sectorId = checkRoomName(room)
#     if sectorId != 0:
#         realRooms.append({'roomName': dashedName, 'sectorId':sectorId})
#         total += sectorId
# print(total)

def cap(num):
    if num > 25:
        return num-25-1
    else:
        return num

def shiftChar(char, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = num % 26
    charIdx = alphabet.index(char)
    newIdx = cap(charIdx + shift)
    return alphabet[newIdx]

def decryptName(name, sectorId):
    temp = ''
    for char in name:
        if char == '-':
            temp+= ' '
        else:
            temp += shiftChar(char, sectorId)

    return temp

# assert decryptName('qzmt-zixmtkozy-ivhz-', 343) == 'very encrypted name '

# decryptNames = []
# for room in realRooms:
#     name = decryptName(room['roomName'], room['sectorId'])
#     decryptNames.append([name,room['sectorId']])
#     print(decryptNames[-1])


#DAY 5 How about a nice game of chess?
import hashlib

def findPassword(id):
    password = ''
    count = 0
    for _ in range(0,8):
        hashhex = ''
        while hashhex[0:5] != '00000':
            hashhex = hashlib.md5(bytes(id+str(count), 'utf-8')).hexdigest()
            count += 1

        password+=hashhex[5]
        # print(hashhex)

    return password

def findPasswordUpdated(id):
    password = [''] * 8
    valids = [str(i) for i in range(0,8)]
    count = 0
    while '' in password:
        hashhex = ''
        while hashhex[0:5] != '00000':
            hashhex = hashlib.md5(bytes(id+str(count), 'utf-8')).hexdigest()
            count += 1

        if hashhex[5] in valids:
            if password[ int(hashhex[5]) ] == '':
                password[ int(hashhex[5]) ] = hashhex[6]
                # print(hashhex)

    password = cat(password)
    return password

#DAY 6 Signals and Noise
data = [i.strip('\n') for i in open('/Users/cloudlife/Desktop/input6.txt').readlines()]

def recover(data):
    msg = ''
    msgLen = len(data[0])
    for i in range(msgLen):
        temp = []
        for row in data:
            temp.append(row[i])

        msg += Counter(temp).most_common(1)[0][0]

    return msg

def recoverLeastCommon(data):
    msg = ''
    msgLen = len(data[0])
    for i in range(msgLen):
        temp = []
        for row in data:
            temp.append(row[i])

        msg += Counter(temp).most_common()[-1][0]

    return msg

#DAY 7 Internet Protocol Version 7
def parse(string):
    start = re.match(r'(\w+)\[.*', string).groups()[0]
    outer = [ele.strip('[]') for ele in re.findall(r'\][a-z]*\[', string)]
    end = re.match(r'.*\]([\w]+)', string).groups()[0]
    inner = [ele.strip('[]') for ele in re.findall(r'\[[a-z]*\]', string)]
    return [start]+outer+[end], inner

def scan(string):
    for idx in range(len(string)-4+1):
        firstHalf = string[idx:idx+2]
        secondHalf = string[idx+2:idx+4]
        # print(firstHalf, secondHalf)
        if firstHalf[0] != firstHalf[1] and firstHalf == secondHalf[::-1]:
            return True
    return False

def checkTLS(data):
    count = 0
    for line in data:
        outer, inner = parse(line)
        if any(map(scan, outer)) == True and any(map(scan, inner)) != True:
            count+=1
    return count

data = fileImport('input7')

def scanABA(string):
    return [string[idx:idx+3] for idx in range(len(string)-3+1) if string[idx] == string[idx+2] and string[idx] != string[idx+1]]

def flipABA(string):
    return string[1] + string[0] + string[1]

def checkSSL(data):
    count = 0
    for line in data:
        outer, inner = parse(line)
        outerABA = set( [flipABA(ele) for ele in mapCombine(scanABA, outer)] )
        innerBAB = set(mapCombine(scanABA, inner))
        if len(outerABA.intersection(innerBAB)) >=1:
            count+=1
    return count

#Day 8 Two-factor Authentication


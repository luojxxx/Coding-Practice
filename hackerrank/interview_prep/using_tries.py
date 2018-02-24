# https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/
class trieNode:
    __slots__ = ['count', 'char', 'childrenDic']
    def __init__(self, char, childrenDic, countInit = 1):
        self.count = countInit
        self.char = char
        self.childrenDic = {}
    def iterateCounter(self):
        self.count += 1
    def addChild(self, char):
        if char not in self.childrenDic:
            childNode = trieNode(char, {})
            self.childrenDic[char] = childNode
            return childNode
        else:
            self.childrenDic[char].iterateCounter()
            return self.childrenDic[char]

def addContact(rootNode, name):
    currentNode = rootNode
    for idx in range(0, len(name) -1):
        char = name[idx]
        nextChar = name[idx+1]
        currentNode = currentNode.addChild(nextChar)

    return rootNode

def findContact(rootNode, name):
    try:
        currentNode = rootNode
        for idx in range(0, len(name) -1):
            char = name[idx]
            nextChar = name[idx+1]
            currentNode = currentNode.childrenDic[nextChar]

        return currentNode.count

    except:
        return 0

contactGraph = trieNode(' ', {}, 0)
def runTrieContacts(op, contact):
    contact = ' '+contact
    if op == 'add':
        addContact(contactGraph, contact)
    if op == 'find':
        print(findContact(contactGraph, contact))
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
def has_cycle(head):
    visitHistory = []
    visitHistory.append(head.data)
    nextNode = head.next
    while nextNode != None:
        if nextNode.data in visitHistory:
            return True
        visitHistory.append(nextNode.data)
        nextNode = nextNode.next
    return False
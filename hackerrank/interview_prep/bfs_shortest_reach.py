# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
import queue
class Graph:
    def __init__(self, n):
        self.dic = {i:[] for i in range(0,n)}

    def connect(self, a, b):
        self.dic[a].append(b)
        self.dic[b].append(a)

    def find_all_distances(self, start):
        visited = [-1 for i in range(len(self.dic))]
        visited[start] = 0
        unvisited = set(list(range(len(self.dic))))
        q = queue.Queue()
        q.put(start)

        while not q.empty():
            currentNode = q.get_nowait()

            distance = visited[currentNode] + 6
            for neighbor in self.dic[currentNode]:
                if neighbor in unvisited:
                    q.put(neighbor)
                    visited[neighbor] = distance
                    unvisited.remove(neighbor)

        del visited[start]

        printStr = ''
        for distance in visited:
            printStr += str(distance) + ' '
        print(printStr)
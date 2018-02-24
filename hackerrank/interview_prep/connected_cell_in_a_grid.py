# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
def findValidNodes(grid):
    validNodeArr = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                validNodeArr.append((i, j))
    return validNodeArr

def adjacentValidNodes(grid, position):
    gridSize_i = len(grid)
    gridSize_j = len(grid[0])
    i = position[0]
    j = position[1]

    adjacentSet = {
    (i-1, j-1),
    (i-1, j+1),
    (i+1, j-1),
    (i+1, j+1),
    (i-1, j),
    (i+1, j),
    (i, j-1),
    (i, j+1)
    }

    validAdjacent = set([])
    for adjacentCoor in adjacentSet:
        if (0 <= adjacentCoor[0] < gridSize_i) and (0 <= adjacentCoor[1] < gridSize_j):
            if grid[adjacentCoor[0]][adjacentCoor[1]] == 1:
                validAdjacent.add(adjacentCoor)

    return validAdjacent

def trip(grid, start):
    visited = set([start])
    stack = list(adjacentValidNodes(grid, start))

    while len(stack) != 0:
        goToCoor = stack.pop()
        visited.add(goToCoor)
        newAdajcentCoor = [coor for coor in adjacentValidNodes(grid, goToCoor)
        if coor not in stack and coor not in visited]
        stack += newAdajcentCoor

    return visited

grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
def getBiggestRegion(grid):
    allValidNodes = set(findValidNodes(grid))
    trips = []

    while len(allValidNodes) != 0:
        start = allValidNodes.pop()
        visited = trip(grid, start)
        trips.append(len(visited))
        allValidNodes = allValidNodes.difference(visited)

    return max(trips)
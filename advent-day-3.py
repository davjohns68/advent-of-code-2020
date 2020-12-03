inputFile = open("day3-input.txt", "r")
treeMap=[]
for item in inputFile:
    treeMap.append(item)

# PARTS 1 & 2
def countTrees(map, cols, rows):
    treeCount = 0
    rowPos = 0
    colPos = 0
    nextRowPos = 0
    nextColPos = 0
    while rowPos < len(map):
        nextRowPos = rowPos + rows
        if nextRowPos >= len(map):
            break
        nextColPos = colPos + cols
        if nextColPos >= len(map[rowPos]) - 1:
            nextColPos -= len(map[rowPos]) - 1
        if treeMap[nextRowPos][nextColPos] == "#":
            treeCount += 1
        rowPos = nextRowPos
        colPos = nextColPos
    return treeCount

first = countTrees(treeMap, 1, 1)
second = countTrees(treeMap, 3, 1)
third = countTrees(treeMap, 5, 1)
fourth = countTrees(treeMap, 7, 1)
fifth = countTrees(treeMap, 1, 2)
totalTreesMult = first * second * third * fourth * fifth
print("Slope 1:1:", first)
print("Slope 3:1:", second)
print("Slope 5:1:", third)
print("Slope 7:1:", fourth)
print("Slope 1:2:", fifth)
print("Total trees encountered multiplied:", totalTreesMult)
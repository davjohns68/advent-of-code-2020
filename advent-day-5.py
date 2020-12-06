inputFile = open("day5-input.txt", "r")
boardingData=[]
for item in inputFile:
    boardingData.append(item.strip('\n'))

# PART 1
highSeatId = 0
for bp in boardingData:
    rowsLow = 0
    rowsHigh = 127
    columnsLow = 0
    columnsHigh = 7
    for i in range(10):
        if bp[i] == "F":
            rowsHigh -= ((rowsHigh - rowsLow) // 2) + 1
        if bp[i] == "B":
            rowsLow += ((rowsHigh - rowsLow) // 2) + 1
        if bp[i] == "L":
            columnsHigh -= ((columnsHigh - columnsLow) // 2) + 1
        if bp[i] == "R":
            columnsLow += ((columnsHigh - columnsLow) // 2) + 1
    seatId = (rowsLow * 8) + columnsLow
    if seatId > highSeatId:
        highSeatId = seatId
    
print(highSeatId)

# PART 2
highSeatId = 0
allSeatIds = []
for bp in boardingData:
    rowsLow = 0
    rowsHigh = 127
    columnsLow = 0
    columnsHigh = 7
    for i in range(10):
        if bp[i] == "F":
            rowsHigh -= ((rowsHigh - rowsLow) // 2) + 1
        if bp[i] == "B":
            rowsLow += ((rowsHigh - rowsLow) // 2) + 1
        if bp[i] == "L":
            columnsHigh -= ((columnsHigh - columnsLow) // 2) + 1
        if bp[i] == "R":
            columnsLow += ((columnsHigh - columnsLow) // 2) + 1
    seatId = (rowsLow * 8) + columnsLow
    allSeatIds.append(seatId)

allSeatIds.sort()
mySeat = 0
for i in range(1, len(allSeatIds) - 1):
    if allSeatIds[i-1] == allSeatIds[i] - 2:
        mySeat = allSeatIds[i] - 1

print(mySeat)
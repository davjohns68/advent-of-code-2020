inputFile = open("day12-input.txt", "r")
navInstructions=[]
for item in inputFile:
    navInstructions.append(item.strip('\n'))

def Rotate(f, i):
    directions = ("N", "E", "S", "W")
    inc = int(i[1:]) // 90
    currentDirection = directions.index(f)
    newDirection = 0
    if i[0] == "R":
        newDirection = currentDirection + inc
    else:
        newDirection = currentDirection - inc
    if newDirection > 3:
        newDirection -= 4
    elif newDirection < 0:
        newDirection += 4
    return directions[newDirection]

def wpRotate(ew, ns, i):
    directions = ("N", "E", "S", "W")
    inc = int(i[1:]) // 90


# PART 1
facing = "E"
ewDist = 0
nsDist = 0
for instruction in navInstructions:
    if instruction[0] == "R" or instruction[0] == "L":
        facing = Rotate(facing, instruction)
    elif instruction[0] == "F":
        if facing == "E":
            ewDist += int(instruction[1:])
        elif facing == "W":
            ewDist -= int(instruction[1:])
        elif facing == "N":
            nsDist += int(instruction[1:])
        elif facing == "S":
            nsDist -= int(instruction[1:])
    elif instruction[0] == "N":
        nsDist += int(instruction[1:])
    elif instruction[0] == "S":
        nsDist -= int(instruction[1:])
    elif instruction[0] == "E":
        ewDist += int(instruction[1:])
    else:
        ewDist -= int(instruction[1:])
    
print("Part 1 Manhattan distance:", abs(ewDist) + abs(nsDist))

# PART 2
facing = "E"
shipEWDist = 0
shipNSDist = 0
wpEWDist = 0
wpNSDist = 0
for instruction in navInstructions:
    if instruction[0] == "R" or instruction[0] == "L":
        facing = Rotate(facing, instruction)
    elif instruction[0] == "F":
        if facing == "E":
            ewDist += int(instruction[1:])
        elif facing == "W":
            ewDist -= int(instruction[1:])
        elif facing == "N":
            nsDist += int(instruction[1:])
        elif facing == "S":
            nsDist -= int(instruction[1:])
    elif instruction[0] == "N":
        nsDist += int(instruction[1:])
    elif instruction[0] == "S":
        nsDist -= int(instruction[1:])
    elif instruction[0] == "E":
        ewDist += int(instruction[1:])
    else:
        ewDist -= int(instruction[1:])
    
print("Part 2 Manhattan distance:", abs(ewDist) + abs(nsDist))
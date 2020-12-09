inputFile = open("day8-input.txt", "r")
operations=[]
for item in inputFile:
    operations.append(item.strip('\n'))

# PART 1
accumulator = 0
step = 0
i = 0
lastStep = 0
lastIndex = 0
penultIndex = 0
lastOp = ""
executedOperations = {}
while i < len(operations):
    opSpl = operations[i].split()
    lastOp = operations[i]
    if opSpl[0] == "nop":
        None
    elif opSpl[0] == "acc":
        accumulator += int(opSpl[1])
    elif opSpl[0] == "jmp":
        penultIndex = i
        i += int(opSpl[1]) - 1
    executedOperations[i] = operations[i]
    i += 1
    step += 1
    if i in executedOperations.keys():
        lastStep = step - 1
        lastIndex = penultIndex
        operations[penultIndex] = 'nop -230'
        break

# PART 2
accumulator = 0
step = 0
i = 0
while i < len(operations):
    if i == penultIndex:
        print(operations[i])
        input("...")
    opSpl = operations[i].split()
    if opSpl[0] == "nop":
        None
    elif opSpl[0] == "acc":
        accumulator += int(opSpl[1])
    elif opSpl[0] == "jmp":
        i += int(opSpl[1]) - 1
    executedOperations[i] = operations[i]
    i += 1
    step += 1
    print("Accumulator:", accumulator, "Index:", penultIndex, "Step:", step, lastOp)
    
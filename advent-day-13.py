inputFile = open("day13-input.txt", "r")
busses=[]
for item in inputFile:
    busses.append(item.strip('\n'))

earliestDep = int(busses[0])
earliestBus = 0
earliestTime = earliestDep * 2
earliestByBus = {}
possibleBusses = busses[1].split(',')
while 'x' in possibleBusses:
    possibleBusses.remove('x')

for bus in possibleBusses:
    bus = int(bus)
    delta = earliestDep % bus
    earliestByBus[bus] = earliestDep + bus - delta

for key in earliestByBus:
    if earliestByBus[key] < earliestTime:
        earliestTime = earliestByBus[key]
        earliestBus = key
    
print(earliestBus * (earliestTime - earliestDep))
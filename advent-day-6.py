inputFile = open("day6-input.txt", "r")
declarationData=[]
for item in inputFile:
    declarationData.append(item.strip('\n'))
dataLength = len(declarationData)

# PART 1 (sum of questions where anyone answered 'yes')
positiveResponses = []
positiveSum = 0
dataCount = 0

for declaration in declarationData:
    dataCount += 1
    for i in range(len(declaration)):
        if declaration[i] not in positiveResponses:
            positiveResponses.append(declaration[i])

    if declaration == '' or dataCount == dataLength:
        positiveSum += len(positiveResponses)
        positiveResponses = []
print(positiveSum)

# PART 2 (sum of questions where EVERYONE in a group answered 'yes')
positiveResponses = []
positiveSum = 0
dataCount = 0
recordCount = 0

for declaration in declarationData:
    dataCount += 1
    recordCount += 1
    for i in range(len(declaration)):
        positiveResponses.append(declaration[i])

    if declaration == '' or dataCount == dataLength:
        if declaration == '':
            recordCount -= 1
        # The set command creates a new list with each item in the target list represented one time
        positiveSet = set(positiveResponses)
        # Rather than iterate through every letter in the alphabet,
        # We can use the set of responses to only test for letters that are present in the responses
        for item in positiveSet:
            if positiveResponses.count(item) == recordCount:
                positiveSum += 1
        positiveResponses = []
        recordCount = 0
print(positiveSum)
inputFile = open("day2-input.txt", "r")
pwsInput=[]
for item in inputFile:
    pwsInput.append(item)

# PART 1
validPasswords = 0
for line in pwsInput:
    temp = line.split()
    countLower = int(temp[0].split('-')[0])
    countUpper = int(temp[0].split('-')[1])
    ruleChar = temp[1].split(':')[0]
    password = temp[2]

    ruleCount = 0
    for char in password:
        if char == ruleChar:
            ruleCount += 1
    if ruleCount >= countLower and ruleCount <= countUpper:
        validPasswords += 1

print(validPasswords)

# PART 2
validPasswords = 0
for line in pwsInput:
    temp = line.split()
    countLower = int(temp[0].split('-')[0])
    countUpper = int(temp[0].split('-')[1])
    ruleChar = temp[1].split(':')[0]
    password = temp[2]

    foundLower = 0
    foundUpper = 0
    if countLower <= len(password):
        if password[countLower - 1] == ruleChar:
            foundLower = 1
    if countUpper <= len(password):
        if password[countUpper - 1] == ruleChar:
            foundUpper = 1
    if foundLower ^ foundUpper:
        validPasswords += 1
    
print(validPasswords)
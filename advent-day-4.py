inputFile = open("day4-input.txt", "r")
passportData=[]
for item in inputFile:
    passportData.append(item.strip('\n'))
numLines = len(passportData)

validPassports = 0
totalPassports = 0
lineCounter = 0
passportRecord = []
for line in passportData:
    lineCounter += 1
    if line != '':
        passportRecord.append(line.split())
    else:
        totalPassports += 1
        passportFlags = 0
        for field in passportRecord:
            for subField in field:
                if "byr" in subField:
                    passportFlags += 128
                if "iyr" in subField:
                    passportFlags += 64
                if "eyr" in subField:
                    passportFlags += 32
                if "hgt" in subField:
                    passportFlags += 16
                if "hcl" in subField:
                    passportFlags += 8
                if "ecl" in subField:
                    passportFlags += 4
                if "pid" in subField:
                    passportFlags += 2
                if "cid" in subField:
                    passportFlags += 1
        if passportFlags == 255 or passportFlags == 254:
            validPassports += 1
        passportRecord = []

    if lineCounter == numLines:
        totalPassports += 1
        passportFlags = 0
        for field in passportRecord:
            for subField in field:
                if "byr" in subField:
                    passportFlags += 128
                if "iyr" in subField:
                    passportFlags += 64
                if "eyr" in subField:
                    passportFlags += 32
                if "hgt" in subField:
                    passportFlags += 16
                if "hcl" in subField:
                    passportFlags += 8
                if "ecl" in subField:
                    passportFlags += 4
                if "pid" in subField:
                    passportFlags += 2
                if "cid" in subField:
                    passportFlags += 1
        if passportFlags == 255 or passportFlags == 254:
            validPassports += 1
        passportRecord = []
        

print("Total passports:", totalPassports)
print("Valid passports:", validPassports)
inputFile = open("day4-input.txt", "r")
passportData=[]
for item in inputFile:
    passportData.append(item.strip('\n'))

validPassports = 0
totalPassports = 0
passportRecord = []
for line in passportData:
    if line != '':
        passportRecord.append(line.split())
    else:
        print(passportRecord)
        totalPassports += 1
        passportFlags = 0
        if "byr" in passportRecord:
            passportFlags += 128
        if "iyr" in passportRecord:
            passportFlags += 64
        if "eyr" in passportRecord:
            passportFlags += 32
        if "hgt" in passportRecord:
            passportFlags += 16
        if "hcl" in passportRecord:
            passportFlags += 8
        if "ecl" in passportRecord:
            passportFlags += 4
        if "pid" in passportRecord:
            passportFlags += 2
        if "cid" in passportRecord:
            passportFlags += 1
        print(passportFlags)
        if passportFlags == 255 or passportFlags == 254:
            validPassports += 1
        input("Press...")
        passportRecord = []

print("Total passports:", totalPassports)
print("Valid passports:", validPassports)
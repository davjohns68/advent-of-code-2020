import re

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
                    byr = int(subField.split(":")[1])
                    if byr >= 1920 and byr <= 2002:
                        passportFlags += 128
                if "iyr" in subField:
                    iyr = int(subField.split(":")[1])
                    if iyr >= 2010 and iyr <=2020:
                        passportFlags += 64
                if "eyr" in subField:
                    eyr = int(subField.split(":")[1])
                    if eyr >= 2020 and eyr <= 2030:
                        passportFlags += 32
                if "hgt" in subField:
                    hgt = subField.split(":")[1]
                    if "cm" in hgt:
                        hgtSpl = int(hgt.split("c")[0])
                        if hgtSpl >= 150 and hgtSpl <= 193:
                            passportFlags += 16
                    if "in" in hgt:
                        hgtSpl = int(hgt.split("i")[0])
                        if hgtSpl >= 59 and hgtSpl <= 76:
                            passportFlags += 16
                if "hcl" in subField:
                    hcl = subField.split(":")[1]
                    x = re.search(r"^#(\d|[a-f]){6}", hcl)
                    if x != None:
                        print(x)
                        passportFlags += 8
                if "ecl" in subField:
                    ecl = subField.split(":")[1]
                    if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl =="oth":
                        passportFlags += 4
                if "pid" in subField:
                    pid = subField.split(":")[1]
                    x = re.search(r"^\d{9}", pid)
                    if x != "None" and len(pid) == 9:
                        passportFlags += 2
                if "cid" in subField:
                    passportFlags += 1

        if passportFlags == 255 or passportFlags == 254:
           #print(passportRecord)
           #print(passportFlags)
           #input("...")
           validPassports += 1
        passportRecord = []
    # This is to handle the last record, which wasn't being handled because there's no '\n' at the end of the file.
        totalPassports += 1
        passportFlags = 0
        for field in passportRecord:
            for subField in field:
                if "byr" in subField:
                    byr = int(subField.split(":")[1])
                    if byr >= 1920 and byr <= 2002:
                        passportFlags += 128
                if "iyr" in subField:
                    iyr = int(subField.split(":")[1])
                    if iyr >= 2010 and iyr <=2020:
                        passportFlags += 64
                if "eyr" in subField:
                    eyr = int(subField.split(":")[1])
                    if eyr >= 2020 and eyr <=2030:
                        passportFlags += 32
                if "hgt" in subField:
                    hgt = subField.split(":")[1]
                    if "cm" in hgt:
                        hgtSpl = int(hgt.split("c")[0])
                        if hgtSpl >= 150 and hgtSpl <= 193:
                            passportFlags += 16
                    if "in" in hgt:
                        hgtSpl = int(hgt.split("i")[0])
                        if hgtSpl >= 59 and hgt <= 76:
                            passportFlags += 16
                if "hcl" in subField:
                    hcl = subField.split(":")[1]
                    x = re.search(r"^#(\d|[a-f]){6}", hcl)
                    if x != "None":
                        passportFlags += 8
                if "ecl" in subField:
                    ecl = subField.split(":")[1]
                    if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl =="oth":
                        passportFlags += 4
                if "pid" in subField:
                    pid = subField.split(":")[1]
                    x = re.search(r"^\d{9}", pid)
                    if x != "None" and len(pid) == 9:
                        passportFlags += 2
                if "cid" in subField:
                    passportFlags += 1

        if passportFlags == 255 or passportFlags == 254:
            validPassports += 1
        passportRecord = []
       

print("Total passports:", totalPassports)
print("Valid passports:", validPassports)
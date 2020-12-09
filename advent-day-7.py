inputFile = open("day7-input.txt", "r")
luggageData=[]
for item in inputFile:
    luggageData.append(item.strip('\n'))
dataLength = len(luggageData)

# PART 1
def getRules(rc, ld, cd):
    for rule in ld:
        if rc in rule:
            if not rule.startswith(rc):
                cd.append(rule)

bagRules = []
nextBagRules = []
colorsTested = ["shiny gold"]
getRules("shiny gold", luggageData, bagRules)
for rule in bagRules:
    ruleSpl = rule.split(" ", 2)
    ruleColor = ruleSpl[0] + " " + ruleSpl[1]
    getRules(ruleColor, luggageData, nextBagRules)
    colorsTested.append(ruleColor)
    nextBagRules = []
print(colorsTested)
print(len(colorsTested))
inputFile = open("input.txt", "r")
expenses=[]
for item in inputFile:
    expenses.append(int(item))
# PART 1
for i in range(0,len(expenses) - 1):
    for j in range(i + 1, len(expenses) - 1):
        if expenses[i] + expenses[j] == 2020:
            print("Part 1 answer:", expenses[i] * expenses[j])

# PART 2
for i in range(0,len(expenses) -1):
    for j in range(i + 1, len(expenses) - 1):
        for k in range(j + 1, len(expenses) - 1):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print("Part 2 answer:", expenses[i] * expenses[j] * expenses[k])
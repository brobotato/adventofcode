lines = open('./input/input7.txt')
processed = []
bots = []  # bots go from 0-209
instructions = {}  # 1 set for every bot. order is low, high
outputs = {}
found = False
temp = 0


def eval(bot, output):
    if not 0 in bots[bot]:
        bot_sorted = sorted(bots[bot])
        if bot_sorted == [17, 61]:
            print(bot)
        if instructions[bot][0][0] == 'bot':
            if bots[int(instructions[bot][0][1])][0] == 0:
                bots[int(instructions[bot][0][1])][0] = bot_sorted[0]
            elif bots[int(instructions[bot][0][1])][1] == 0:
                bots[int(instructions[bot][0][1])][1] = bot_sorted[0]
        else:
            output[int(instructions[bot][0][1])] = bot_sorted[0]
        if instructions[bot][1][0] == 'bot':
            if bots[int(instructions[bot][1][1])][0] == 0:
                bots[int(instructions[bot][1][1])][0] = bot_sorted[1]
            elif bots[int(instructions[bot][1][1])][1] == 0:
                bots[int(instructions[bot][1][1])][1] = bot_sorted[1]
        else:
            output[int(instructions[bot][1][1])] = bot_sorted[1]
        bots[bot] = [0, 0]


for x in range(210):
    bots.append([0, 0])
for l in lines:
    processed.append(l.split())
for line in processed:
    if line[0] == 'value' and bots[int(line[-1])][0] == 0:
        bots[int(line[-1])][0] = int(line[1])
    elif line[0] == 'value':
        bots[int(line[-1])][1] = int(line[1])
    elif line[0] == 'bot':
        instructions[int(line[1])] = (line[5:7], line[10:])
while temp < 5000:
    for x in range(210):
        eval(x, outputs)
        temp += 1
print(outputs)

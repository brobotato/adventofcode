lines = open('./input/input3.txt')
processed = []
frequency = [{}, {}, {}, {}, {}, {}, {}, {}]
part1 = []
part2 = []
for l in lines:
    processed.append(l.split())
for p in processed:
    for l in p:
        for x in range(len(l)):
            try:
                frequency[x][l[x]] += 1
            except KeyError:
                frequency[x][l[x]] = 1
for x in range(len(frequency)):
    for v in frequency[x]:
        if frequency[x][v] == 22:
            part1.append(v)
        elif frequency[x][v] == 20:
            part2.append(v)
print(''.join(part1), '\n', ''.join(part2))

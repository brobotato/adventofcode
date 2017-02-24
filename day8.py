lines = open('./input/input5.txt')
processed = []
instructions = []
w, h = 50, 6;
keypad = [[0 for x in range(w)] for y in range(h)]
ones = 0


# keypad[y][x]
def rotate_x(line, shift):
    shift %= 50
    output = keypad[line][-shift:] + keypad[line][:-shift]
    keypad[line] = output


def rotate_y(column, shift):
    output = [0, 0, 0, 0, 0, 0]
    for x in range(6):
        new = (x + shift) % 6
        output[new] = keypad[x][column]
    keypad[0][column], keypad[1][column], keypad[2][column], keypad[3][column], keypad[4][column], keypad[5][
        column] = output


def generate_rect(w, h):
    for x in range(w):
        for y in range(h):
            keypad[y][x] = 1


for l in lines:
    processed.append(l.split())
for p in processed:
    if p[0] == 'rect':
        try:
            instructions.append([int(p[1][0]), int(p[1][2]), 'rect'])
        except ValueError:
            instructions.append([int(p[1][0:2]), int(p[1][3]), 'rect'])
    elif p[0] == 'rotate':
        if p[1] == 'column':
            instructions.append([int(p[2][2:]), int(p[4]), 'y'])
        else:
            instructions.append([int(p[2][2:]), int(p[4]), 'x'])
for i in instructions:
    if i[2] == 'rect':
        generate_rect(i[0], i[1])
    if i[2] == 'y':
        rotate_y(i[0], i[1])
    if i[2] == 'x':
        rotate_x(i[0], i[1])
for k in keypad:
    for char in k:
        if char == 1:
            ones += 1
    print(k)
print(ones)
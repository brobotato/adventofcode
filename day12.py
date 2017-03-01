import time

instructions = [l.split() for l in open('./input/input8.txt')]
values = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
currentinstruction = 0


def evaluate(instruction):
    global values
    global currentinstruction
    if instructions[instruction][0] == 'cpy':
        try:
            values[instructions[instruction][2]] = int(instructions[instruction][1])
        except ValueError:
            values[instructions[instruction][2]] = values[instructions[instruction][1]]
        currentinstruction += 1
    if instructions[instruction][0] == 'inc':
        values[instructions[instruction][1]] += 1
        currentinstruction += 1
    if instructions[instruction][0] == 'dec':
        values[instructions[instruction][1]] -= 1
        currentinstruction += 1
    if instructions[instruction][0] == 'jnz':
        try:
            if values[instructions[instruction][1]] != 0:
                currentinstruction += int(instructions[instruction][2])
            else:
                currentinstruction += 1
        except KeyError:
            currentinstruction += int(instructions[instruction][2])


while currentinstruction < len(instructions):
    evaluate(currentinstruction)
print(values['a'])

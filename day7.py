import re

lines = open('./input/input4.txt')
processed = []
hypernet_sequences = []
valid = 0


def abba(string):
    if string[0:3] == string[3:0:-1] and string[0] != string[1]:
        return True


def check_abba(string):
    valid = False
    for x in range(len(string) - 3):
        if abba(string[x:x + 4]):
            valid = True
    return valid


def check_hyper(sequence):
    valid = True
    for s in sequence:
        if check_abba(s):
            valid = False
    return valid


for l in lines:
    processed.append(l.split())
for p in processed:
    for l in p:
        hypernet_sequences.append(re.findall('\[([^[\]]*)\]', l))
for x in range(len(processed)):
    if not check_hyper(processed[x]) and check_hyper(hypernet_sequences[x]):
        valid += 1
print(valid)

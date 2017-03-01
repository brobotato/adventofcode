mult_list = []
final_length = 0


def search(string, base, list):
    start = string.index('(') + 1
    end = string.index(')') + 1
    first_x = string.index('x')
    length = int(string[start:first_x])
    multiplier = int(string[first_x + 1:end - 1]) * base
    to_be_multiplied = string[end:end + length]
    temp = string.replace(to_be_multiplied, '')
    final = temp.replace(string[start - 1:end], '')
    list.append([to_be_multiplied, multiplier])
    return final


with open('./input/input6.txt') as lines:
    for l in lines:
        input = l.split()
input.append(1)
while len(input[0]) > 20:
    input[0] = search(input[0], input[1], mult_list)
for m in mult_list:
    final_length += len(m[0]) * m[1]
final_length += len(input[0])
print(final_length)
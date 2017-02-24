def valid_tri(x):
    s1, s2, s3 = x
    s1, s2, s3 = round(int(float(s1))), round(int(float(s2))), round(int(float(s3)))
    a1 = s1 + s2
    a2 = s1 + s3
    a3 = s2 + s3
    if (a1 > s3) and (a2 > s2) and (a3 > s1):
        return True
    else:
        return False


lines = open('./input/input1.txt')
processed = []
processed2 = []
valid = 0
for l in lines:
    processed.append(l.split())
for x in range(0, 3, 1):
    for y in range(0, len(processed), 3):
        processed2.append([processed[y][x], processed[y + 1][x], processed[y + 2][x]])
for p in processed2:
    if valid_tri(p):
        valid += 1
print(valid)

# part 1 was also much easier.
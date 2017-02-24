import operator, string

lines = open('./input/input2.txt')
processed = []
keys = []
keyssorted = []
checksums = []
sector_ids = []
sum = 0
real_rooms = []
room_names = []
morse = {}
morse_reverse = {}
northpole = 0
for x in range(len(string.ascii_lowercase)):
    morse[x] = string.ascii_lowercase[x]
for x in range(len(string.ascii_lowercase)):
    morse_reverse[string.ascii_lowercase[x]] = x


def remove_dashes(string):
    dashes = 0
    for x in range(len(string)):
        if string[x] == '-':
            dashes += 1
    return string[dashes:]


def shift(string, dist):
    asnum = [morse_reverse[x] for x in list(string)]
    shifted = []
    final = []
    for a in asnum:
        a += dist
        a %= 26
        shifted.append(a)
    for s in shifted:
        final.append(morse[s])
    return ''.join(final)


def alphabetize(list):
    tempdict = {}
    templist = []
    templist2 = []
    for l in list:
        if not l[1] in tempdict:
            tempdict[l[1]] = 1
        else:
            tempdict[l[1]] += 1
    for l in list:
        if tempdict[l[1]] > 1:
            templist.append([l[1], list.index(l)])
    for p in templist:
        if not p[0] in templist2:
            templist2.append(p[0])
    for w in templist2:
        lulu = [p for p in templist if p[0] == w]
        x, y = min([l[1] for l in lulu]), max(l[1] for l in lulu)
        list[x:y + 1] = sorted(list[x:y + 1])
    return ''.join([l[0] for l in list][:5])


def by_frequency(string):
    lettercount = {}
    for x in string:
        lettercount[x] = 0
    for x in string:
        lettercount[x] += 1
    return [list(l) for l in lettercount.items()]


for l in lines:
    processed.append(l.split())
for x in range(len(processed)):
    keys.append(remove_dashes(sorted(processed[x][0][:-10])))
    checksums.append(processed[x][0][-6:-1])
    sector_ids.append(processed[x][0][-10:-7])
for k in keys:
    keyssorted.append(by_frequency(k))
for x in keyssorted:
    x.sort(key=operator.itemgetter(1), reverse=True)
for x in range(len(processed)):
    if alphabetize(keyssorted[x]) == checksums[x]:
        sum += int(sector_ids[x])
        real_rooms.append(processed[x])
for x in range(len(real_rooms)):
    room_names.append(real_rooms[x][0][:-10].split('-')[:-1])
for x in range(len(room_names)):
    for r in room_names[x]:
        if shift(r, int(real_rooms[x][0][-10:-7])) == 'northpole':
            northpole = r
for r in room_names:
    if northpole in r:
        print(real_rooms[room_names.index(r)])

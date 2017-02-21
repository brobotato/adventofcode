keypad = [0, 0, 1, 0, 0,
          0, 2, 3, 4, 0,
          5, 6, 7, 8, 9,
          0, 'A', 'B', 'C', 0,
          0, 0, 'D', 0, 0]
set1 = 'LRRLLLRDRURUDLRDDURULRULLDLRRLRLDULUDDDDLLRRLDUUDULDRURRLDULRRULDLRDUDLRLLLULDUURRRRURURULURRULRURDLULURDRDURDRL' \
       'RRUUDRULLLLLDRULDDLLRDLURRLDUURDLRLUDLDUDLURLRLDRLUDUULRRRUUULLRDURUDRUDRDRLLDLDDDLDLRRULDUUDULRUDDRLLURDDRLDDUD' \
       'LLLLULRDDUDDUUULRULUULRLLDULUDLLLLURRLDLUDLDDLDRLRRDRDUDDDLLLLLRRLLRLUDLULLDLDDRRUDDRLRDDURRDULLLURLRDLRRLRDLDUR' \
       'LDDULLLDRRURDULUDUDLLLDDDLLRLDDDLLRRLLURUULULDDDUDULUUURRUUDLDULULDRDDLURURDLDLULDUDUDDDDD'
set2 = 'RUURUDRDUULRDDLRLLLULLDDUDRDURDLRUULLLLUDUDRRUDUULRRUUDDURDDDLLLLRRUURULULLUDDLRDUDULRURRDRDLDLDUULUULUDDLUDRLUL' \
       'RUDRDDDLRRUUDRRLULUULDULDDLRLURDRLURRRRULDDRLDLLLRULLDURRLUDULDRDUDRLRLULRURDDRLUDLRURDDRDULUDLDLLLDRLRUDLLLLLDU' \
       'DRDUURUDDUDLDLDUDLLDLRRDLULLURLDDUDDRDUDLDDUULDRLURRDLDLLUUDLDLURRLDRDDLLDLRLULUDRDLLLDRLRLLLDRUULUDLLURDLLUURUD' \
       'URDDRDRDDUDDRRLLUULRRDRULRURRULLDDDUDULDDRULRLDURLUDULDLDDDLRULLULULUDLDDRDLRDRDLDULRRLRLRLLLLLDDDRDDULRDULRRLDL' \
       'UDDDDLUDRLLDLURDLRDLDRDRDURRDUDULLLDLUDLDRLRRDDDRRLRLLULDRLRLLLLDUUURDLLULLUDDRLULRDLDLDURRRUURDUDRDLLLLLLDDDURL' \
       'DULDRLLDUDRULRRDLDUDRLLUUUDULURRUR'
set3 = 'URRRLRLLDDDRRLDLDLUDRDRDLDUDDDLDRRDRLDULRRDRRDUDRRUUDUUUDLLUURLRDRRURRRRUDRLLLLRRDULRDDRUDLRLUDURRLRLDDRRLUULURL' \
       'URURUDRULDUUDLULUURRRDDLRDLUDRDLDDDLRUDURRLLRDDRDRLRLLRLRUUDRRLDLUDRURUULDUURDRUULDLLDRDLRDUUDLRLRRLUDRRUULRDDRD' \
       'LDDULRRRURLRDDRLLLRDRLURDLDRUULDRRRLURURUUUULULRURULRLDDDDLULRLRULDUDDULRUULRRRRRLRLRUDDURLDRRDDULLUULLDLUDDDUUR' \
       'LRRLDULUUDDULDDUULLLRUDLLLRDDDLUUURLDUDRLLLDRRLDDLUDLLDLRRRLDDRUULULUURDDLUR'
set4 = 'UULDRLUULURDRLDULURLUDULDRRDULULUDLLDURRRURDRLRLLRLDDLURRDLUUDLULRDULDRDLULULULDDLURULLULUDDRRULULULRDULRUURRRUD' \
       'LRLURDRURDRRUDLDDUURDUUDLULDUDDLUUURURLRRDLULURDURRRURURDUURDRRURRDDULRULRRDRRDRUUUUULRLUUUDUUULLRRDRDULRDDULDRR' \
       'ULRLDLLULUUULUUDRDUUUDLLULDDRRDULUURRDUULLUUDRLLDUDLLLURURLUDDLRURRDRLDDURLDLLUURLDUURULLLRURURLULLLUURUUULLDLRD' \
       'LUDDRRDDUUDLRURDDDRURUURURRRDLUDRLUULDUDLRUUDRLDRRDLDLDLRUDDDDRRDLDDDLLDLULLRUDDUDDDLDDUURLDUDLRDRURULDULULUDRRD' \
       'LLRURDULDDRRDLUURUUULULRURDUUDLULLURUDDRLDDUDURRDURRUURLDLLDDUUDLLUURDRULLRRUUURRLLDRRDLURRURDULDDDDRDD'
set5 = 'LLRUDRUUDUDLRDRDRRLRDRRUDRDURURRLDDDDLRDURDLRRUDRLLRDDUULRULURRRLRULDUURLRURLRLDUDLLDULULDUUURLRURUDDDDRDDLLURDL' \
       'DRRUDRLDULLRULULLRURRLLURDLLLRRRRDRULRUDUDUDULUURUUURDDLDRDRUUURLDRULDUDULRLRLULLDURRRRURRRDRULULUDLULDDRLRRULLD' \
       'URUDDUULRUUURDRRLULRRDLDUDURUUUUUURRUUULURDUUDLLUURDLULUDDLUUULLDURLDRRDDLRRRDRLLDRRLUDRLLLDRUULDUDRDDRDRRRLUDUD' \
       'RRRLDRLRURDLRULRDUUDRRLLRLUUUUURRURLURDRRUURDRRLULUDULRLLURDLLULDDDLRDULLLUDRLURDDLRURLLRDRDULULDDRDDLDDRUUURDUU' \
       'UDURRLRDUDLRRLRRRDUULDRDUDRLDLRULDL'

oob = [[0, 0], [1, 0], [3, 0], [4, 0], [0, 1], [4, 1], [0, 3], [4, 3], [0, 4], [1, 4], [3, 4], [4, 4]]
bounds = []
for x in range(0, 5, 1):
    for y in range(0, 5, 1):
        bounds.append([x, y])
for x in oob:
    if x in bounds:
        bounds.remove(x)


class set:
    def __init__(self, x, y):
        self.set = x
        self.output = y
        self.number = 0

    def calculate(self):
        for x in range(0, len(self.set), 1):
            if self.set[x] == 'U':
                self.output[1] -= 1
                if self.output in bounds and not self.output in oob:
                    pass
                else:
                    self.output[1] += 1
            if self.set[x] == 'D':
                self.output[1] += 1
                if self.output in bounds and not self.output in oob:
                    pass
                else:
                    self.output[1] -= 1
            if self.set[x] == 'L':
                self.output[0] -= 1
                if self.output in bounds and not self.output in oob:
                    pass
                else:
                    self.output[0] += 1
            if self.set[x] == 'R':
                self.output[0] += 1
                if self.output in bounds and not self.output in oob:
                    pass
                else:
                    self.output[0] -= 1
        self.number = keypad[self.output[0] + self.output[1] * 5]
        print(self.number)
        print(self.output)


dir1 = set(set1, [0, 3])
dir1.calculate()
dir2 = set(set2, dir1.output)
dir2.calculate()
dir3 = set(set3, dir2.output)
dir3.calculate()
dir4 = set(set4, dir3.output)
dir4.calculate()
dir5 = set(set5, dir4.output)
dir5.calculate()

# part 1 was much easier. dont think solution needs to be included
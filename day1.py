import math, turtle

coords = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5,' \
         ' L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2,' \
         ' L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5,' \
         ' R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5,' \
         ' R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1,' \
         ' L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5,' \
         ' R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'
pcoords = coords.split(', ')
rcoords = [0, 0]
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(1)
turtle.hideturtle()
locationsvisited = []
angle = -90
for x in pcoords:
    if x[0] == 'R':
        angle += 90
    if x[0] == 'L':
        angle -= 90
    rcoords[0] += math.cos(math.radians(angle)) * int(float(x[1:]))
    rcoords[0] = round(rcoords[0])
    rcoords[1] += math.sin(math.radians(angle)) * int(float(x[1:]))
    rcoords[1] = round(rcoords[1])
    locationsvisited.append((rcoords[0], rcoords[1]))
for x in locationsvisited:
    turtle.setpos(x[0], x[1])  # take a screenshot to find how far away the intersection is
print(turtle.position())  # answer to part 1

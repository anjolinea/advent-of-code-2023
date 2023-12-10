# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ

LINES = []

with open("input.txt") as f:
    for line in f:
        LINES.append(list(line.strip()))

temp = 0
for x in range(len(LINES)):
    for y in range(len(LINES[0])):
        if LINES[x][y] == "S":
            CURRENT = (x,y)
        if LINES[x][y] == ".":
            temp += 1

print(temp)
START = True
STEPS = 0
MAX_Y = len(LINES[0])
MAX_X = len(LINES)
DIR = None

while LINES[CURRENT[0]][CURRENT[1]] != "S" or START:
    x = CURRENT[0]
    y = CURRENT[1]
    symbol = LINES[CURRENT[0]][CURRENT[1]]
    if START:
        START = False
        # west S X
        if y+1 < MAX_Y:
            if LINES[x][y+1] in ["J", "-", "7"]:
                CURRENT = (x, y+1)
                DIR = "WEST"
        # east X S
        elif y-1 >= 0:
            if LINES[x][y+1] in ["F", "-", "L"]:
                CURRENT = (x, y-1)
                DIR = "EAST"
        # north X S
        elif x-1 >= 0:
            if LINES[x-1][y] in ["|", "F", "7"]:
                CURRENT = (x-1, y)
                DIR = "NORTH"
        elif x+1 < MAX_X:
            if LINES[x+1][y] in ["|", "L", "J"]:
                CURRENT = (x+1, y)
                DIR = "SOUTH"
    else:
        # WEST
        if DIR == "WEST":
            if symbol == "J":
                CURRENT = (x-1, y)
                DIR = "NORTH"
            elif symbol == "-":
                CURRENT = (x, y+1)
                DIR = "WEST"
            elif symbol == "7":
                CURRENT = (x+1, y)
                DIR = "SOUTH"
        # EAST
        elif DIR == "EAST":
            if symbol == "F":
                CURRENT = (x+1, y)
                DIR = "SOUTH"
            elif symbol == "-":
                CURRENT = (x, y-1)
                DIR = "EAST"
            elif symbol == "L":
                CURRENT = (x-1, y)
                DIR = "NORTH"
        # SOUTH
        if DIR == "SOUTH":
            if symbol == "|":
                CURRENT = (x+1, y)
                DIR = "SOUTH"
            elif symbol == "L":
                CURRENT = (x, y+1)
                DIR = "WEST"
            elif symbol == "J":
                CURRENT = (x, y-1)
                DIR = "EAST"
        # SOUTH
        if DIR == "NORTH":
            if symbol == "|":
                CURRENT = (x-1, y)
                DIR = "NORTH"
            elif symbol == "F":
                CURRENT = (x, y+1)
                DIR = "WEST"
            elif symbol == "7":
                CURRENT = (x, y-1)
                DIR = "EAST"
    STEPS += 1

print(STEPS // 2)
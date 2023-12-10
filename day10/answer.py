# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ

LINES = []

with open("input.txt") as f:
    for line in f:
        LINES.append(list(line.strip()))

def part_one():
    for x in range(len(LINES)):
        for y in range(len(LINES[0])):
            if LINES[x][y] == "S":
                CURRENT = (x,y)

    START = True
    STEPS = 0
    MAX_Y = len(LINES[0])
    MAX_X = len(LINES)
    DIR = None

    while LINES[CURRENT[0]][CURRENT[1]] != "S" or START:
        x = CURRENT[0]
        y = CURRENT[1]
        symbol = LINES[x][y]
        if START:
            START = False
            # west S X
            if y+1 < MAX_Y:
                if LINES[x][y+1] in ["J", "-", "7"]:
                    CURRENT = (x, y+1)
                    DIR = "WEST"
            # east X S
            elif y-1 >= 0:
                if LINES[x][y-1] in ["F", "-", "L"]:
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

def part_two():
    for x in range(len(LINES)):
        for y in range(len(LINES[0])):
            if LINES[x][y] == "S":
                CURRENT = (x,y)

    START = True
    MAX_Y = len(LINES[0])
    MAX_X = len(LINES)

    NOT_VERTICAL = 0
    TOP_VERTICAL = 1
    BOTTOM_VERTICAL = 2
    # DIR => prev -----> current direction
    DIR = None
    VERT = [[NOT_VERTICAL for _ in range(MAX_Y)] for _ in range(MAX_X)]
    VISITED = [[False for _ in range(MAX_Y)] for _ in range(MAX_X)]

    while LINES[CURRENT[0]][CURRENT[1]] != "S" or START:
        x = CURRENT[0]
        y = CURRENT[1]
        VISITED[x][y] = True
        symbol = LINES[x][y]
        if START:
            START = False
            INCOMPLETE = True
            # west S X
            if y+1 < MAX_Y:
                if LINES[x][y+1] in ["J", "-", "7"]:
                    CURRENT = (x, y+1)
                    DIR = "WEST"
                    INCOMPLETE = False
            # east X S
            if INCOMPLETE and y-1 >= 0:
                if LINES[x][y-1] in ["F", "-", "L"]:
                    CURRENT = (x, y-1)
                    DIR = "EAST"
                    INCOMPLETE = False
            # north X S
            if INCOMPLETE and x-1 >= 0:
                if LINES[x-1][y] in ["|", "F", "7"]:
                    CURRENT = (x-1, y)
                    DIR = "NORTH"
                    INCOMPLETE = False
            # SOUTH
            if INCOMPLETE and x+1 < MAX_X:
                if LINES[x+1][y] in ["|", "L", "J"]:
                    CURRENT = (x+1, y)
                    DIR = "SOUTH"
                    INCOMPLETE = False

            # hardcoded by inspection ==> What is S? a L, J, etc.
            VERT[x][y] = BOTTOM_VERTICAL
        else:
            # WEST x J
            if DIR == "WEST":
                if symbol == "J":
                    VERT[x][y] = TOP_VERTICAL
                    CURRENT = (x-1, y)
                    DIR = "NORTH"
                elif symbol == "-":
                    CURRENT = (x, y+1)
                    DIR = "WEST"
                elif symbol == "7":
                    VERT[x][y] = BOTTOM_VERTICAL
                    CURRENT = (x+1, y)
                    DIR = "SOUTH"
            # EAST
            elif DIR == "EAST":
                if symbol == "F":
                    VERT[x][y] = BOTTOM_VERTICAL
                    CURRENT = (x+1, y)
                    DIR = "SOUTH"
                elif symbol == "-":
                    CURRENT = (x, y-1)
                    DIR = "EAST"
                elif symbol == "L":
                    VERT[x][y] = TOP_VERTICAL
                    CURRENT = (x-1, y)
                    DIR = "NORTH"
            # SOUTH
            if DIR == "SOUTH":
                if symbol == "|":
                    CURRENT = (x+1, y)
                    DIR = "SOUTH"
                elif symbol == "L":
                    VERT[x][y] = TOP_VERTICAL
                    CURRENT = (x, y+1)
                    DIR = "WEST"
                elif symbol == "J":
                    VERT[x][y] = TOP_VERTICAL
                    CURRENT = (x, y-1)
                    DIR = "EAST"
            # SOUTH
            if DIR == "NORTH":
                if symbol == "|":
                    CURRENT = (x-1, y)
                    DIR = "NORTH"
                elif symbol == "F":
                    VERT[x][y] = BOTTOM_VERTICAL
                    CURRENT = (x, y+1)
                    DIR = "WEST"
                elif symbol == "7":
                    VERT[x][y] = BOTTOM_VERTICAL
                    CURRENT = (x, y-1)
                    DIR = "EAST"
    
    ans = 0
    for x in range(len(LINES)):
        #NUM_VERTICAL_PIPES = 0
        NUM_TOP_VERTICAL = 0
        NUM_BOTTOM_VERTICAL = 0
        for y in range(len(LINES[0])):
            symbol = LINES[x][y]
            vert = VERT[x][y]
            if not(VISITED[x][y]) and min(NUM_BOTTOM_VERTICAL, NUM_TOP_VERTICAL) % 2 == 1:
                ans += 1
            elif symbol == "|" and VISITED[x][y]:
                NUM_TOP_VERTICAL += 1
                NUM_BOTTOM_VERTICAL += 1
            elif symbol in ["J", "F", "7", "L", "S"] and VISITED[x][y]:
                if vert == BOTTOM_VERTICAL:
                    NUM_BOTTOM_VERTICAL += 1
                elif vert == TOP_VERTICAL:
                    NUM_TOP_VERTICAL += 1

    print(ans)
            
part_two()

from collections import deque

LINES = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        LINES.append(list(line))

MAX_X = len(LINES)
MAX_Y = len(LINES[0])

def process_entrypoint(entrypoint):
    visited = set([entrypoint])
    queue = deque([entrypoint])
    while len(queue) != 0:
        x, y, dir = queue.popleft()
        c = LINES[x][y]
        match c:
            case ".":
                match dir:
                    case "R":
                        if y+1 < MAX_Y and (x, y+1, "R") not in visited:
                            visited.add((x, y+1, "R"))
                            queue.append((x, y+1, "R"))
                    case "L":
                        if y-1 >= 0 and (x, y-1, "L") not in visited:
                            visited.add((x, y-1, "L"))
                            queue.append((x, y-1, "L")) 
                    case "U":
                        if x-1 >= 0 and (x-1, y, "U") not in visited:
                            visited.add((x-1, y, "U"))
                            queue.append((x-1, y, "U"))
                    case "D":
                        if x+1 < MAX_X and (x+1, y, "D") not in visited:
                            visited.add((x+1, y, "D"))
                            queue.append((x+1, y, "D")) 
            case "\\":
                match dir:
                    case "D":
                        if y+1 < MAX_Y and (x, y+1, "R") not in visited:
                            visited.add((x, y+1, "R"))
                            queue.append((x, y+1, "R"))
                    case "U":
                        if y-1 >= 0 and (x, y-1, "L") not in visited:
                            visited.add((x, y-1, "L"))
                            queue.append((x, y-1, "L")) 
                    case "L":
                        if x-1 >= 0 and (x-1, y, "U") not in visited:
                            visited.add((x-1, y, "U"))
                            queue.append((x-1, y, "U"))
                    case "R":
                        if x+1 < MAX_X and (x+1, y, "D") not in visited:
                            visited.add((x+1, y, "D"))
                            queue.append((x+1, y, "D")) 
            case "/":
                match dir:
                    case "U":
                        if y+1 < MAX_Y and (x, y+1, "R") not in visited:
                            visited.add((x, y+1, "R"))
                            queue.append((x, y+1, "R"))
                    case "D":
                        if y-1 >= 0 and (x, y-1, "L") not in visited:
                            visited.add((x, y-1, "L"))
                            queue.append((x, y-1, "L")) 
                    case "R":
                        if x-1 >= 0 and (x-1, y, "U") not in visited:
                            visited.add((x-1, y, "U"))
                            queue.append((x-1, y, "U"))
                    case "L":
                        if x+1 < MAX_X and (x+1, y, "D") not in visited:
                            visited.add((x+1, y, "D"))
                            queue.append((x+1, y, "D")) 
            case "-":
                match dir:
                    case "R":
                        if y+1 < MAX_Y and (x, y+1, "R") not in visited:
                            visited.add((x, y+1, "R"))
                            queue.append((x, y+1, "R"))
                    case "L":
                        if y-1 >= 0 and (x, y-1, "L") not in visited:
                            visited.add((x, y-1, "L"))
                            queue.append((x, y-1, "L")) 
                    case "U" | "D":
                        if y+1 < MAX_Y and (x, y+1, "R") not in visited:
                            visited.add((x, y+1, "R"))
                            queue.append((x, y+1, "R"))
                        if y-1 >= 0 and (x, y-1, "L") not in visited:
                            visited.add((x, y-1, "L"))
                            queue.append((x, y-1, "L")) 
            case "|":
                match dir:
                    case "U":
                        if x-1 >= 0 and (x-1, y, "U") not in visited:
                            visited.add((x-1, y, "U"))
                            queue.append((x-1, y, "U"))
                    case "D":
                        if x+1 < MAX_X and (x+1, y, "D") not in visited:
                            visited.add((x+1, y, "D"))
                            queue.append((x+1, y, "D")) 
                    case "L" | "R":
                        if x-1 >= 0 and (x-1, y, "U") not in visited:
                            visited.add((x-1, y, "U"))
                            queue.append((x-1, y, "U"))
                        if x+1 < MAX_X and (x+1, y, "D") not in visited:
                            visited.add((x+1, y, "D"))
                            queue.append((x+1, y, "D")) 

    return len(set([tuple(x[:2]) for x in list(visited)]))

def part_one():
    print(process_entrypoint((0,0,"R")))

def part_two():
    ans = 0
    for i in range(MAX_X):
        ans = max(ans, process_entrypoint((i,0,"R")))
        ans = max(ans, process_entrypoint((i,MAX_Y-1,"L")))

    for i in range(MAX_Y):
        ans = max(ans, process_entrypoint((0,i,"D")))
        ans = max(ans, process_entrypoint((MAX_X-1,i,"U")))

    print(ans)

part_one()
part_two()




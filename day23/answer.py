import sys

sys.setrecursionlimit(100000)

grid = []
POSSIBLE_MOVES = [(-1,0), (1,0), (0,1), (0,-1)]

with open("input.txt") as fhand:
    for line in fhand:
        line = line.strip()
        grid.append(list(line))

MAX_X = len(grid)
MAX_Y = len(grid[0])

# modify grid so we don't have to check bounds
grid[0][1] = "#"

start = (1,1)
end = (MAX_X - 1, MAX_Y - 2)

path_lengths = set()

def get_next_steps(current, part):
    x, y = current
    symbol = grid[x][y]
    if part == "one":
        if symbol == ">":
            return [(x, y+1)]
        elif symbol == "<":
            return [(x, y-1)]
        elif symbol == "v":
            return [(x+1, y)]
        elif symbol == "^":
            return [(x-1, y)]
    return list(filter(lambda z: grid[z[0]][z[1]] != "#", [(x + x1, y + y1) for x1, y1 in POSSIBLE_MOVES]))

visited = [[False for _ in range(MAX_Y)] for _ in range(MAX_X)]
cur_max = 0

def dfs(current, path_length, part):
    global cur_max

    x, y = current
    visited[x][y] = True
    if current == end:
        if path_length > cur_max:
            cur_max = path_length
    else:
        next_steps = get_next_steps(current, part)
        for ns in next_steps:
            if not visited[ns[0]][ns[1]]:
                dfs(ns, path_length+1, part)

    visited[x][y] = False

dfs(start,1,"one") # do "one" or "two"
print(cur_max)




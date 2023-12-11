LINES = []

with open("input.txt") as f:
    for line in f:
        LINES.append(list(line.strip()))

def check_all_dots_rows(line):
    for x in line:
        if x != ".":
            return False
    return True

def check_all_dots_columns(i):
    for j in range(len(LINES)):
        if LINES[j][i] != ".":
            return False
    return True

to_add_rows = [i for i, line in enumerate(LINES) if check_all_dots_rows(line)]
to_add_columns = [i for i in range(len(LINES[0])) if check_all_dots_columns(i)]

MEGA_ROWS = []
MEGA_COLUMNS = []
for add in to_add_rows:
    MEGA_ROWS.append(add)

surplus = 0
for add in to_add_columns:
    MEGA_COLUMNS.append(add)

MAX_X = len(LINES)
MAX_Y = len(LINES[0])
GALAXIES = []
for x in range(MAX_X):
    for y in range(MAX_Y):
        if LINES[x][y] == "#":
            GALAXIES.append((x,y))

def process(extra_length):
    ans = 0
    for i in range(len(GALAXIES)):
        x_a, y_a = GALAXIES[i]
        for j in range(i, len(GALAXIES)):
            x_b, y_b = GALAXIES[j]
            bigger_x = max(x_a, x_b)
            smaller_x = min(x_a, x_b)
            bigger_y = max(y_a, y_b)
            smaller_y = min(y_a, y_b)
            x_diff = 0
            for x_t in range(smaller_x+1, bigger_x+1):
                if x_t in MEGA_ROWS:
                    x_diff += extra_length
                else:
                    x_diff += 1
            y_diff = 0
            for y_t in range(smaller_y+1, bigger_y+1):
                if y_t in MEGA_COLUMNS:
                    y_diff += extra_length
                else:
                    y_diff += 1

            ans += x_diff + y_diff

    print(ans)

def part_one():
    process(2)

def part_two():
    process(1000000)

part_one()
part_two()
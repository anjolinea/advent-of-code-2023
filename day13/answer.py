GRIDS = []
current_grid = []

with open("input.txt", "r") as fhand:
    for line in fhand:
        if line == "\n":
            GRIDS.append(current_grid)
            current_grid = []
        else:
            current_grid.append(list(line.strip()))


def process_grid(grid, part_one=True):
    # reduce to row and column numbers
    row_nums = []
    for row in grid:
        num = 0
        for i, c in enumerate(row):
            if c == "#":
                num += 2 ** i
        row_nums.append(num)

    column_nums = []
    for i in range(len(grid[0])):
        num = 0
        for j, row in enumerate(grid):
            c = row[i]
            if c == "#":
                num += 2 ** j
        column_nums.append(num)

    def process_arr(arr):

        def check(mirror):
            bef = mirror
            aft = mirror + 1
            while bef >= 0 and aft < len(arr) and arr[bef] == arr[aft]:
                bef -= 1
                aft += 1
            if bef < 0 or aft >= len(arr):
                return True
            return False

        to_return =[]
        for i in range(len(arr)-1):
            if check(i):
                to_return.append(i+1)
        
        return to_return

    hor = [100 * x for x in process_arr(row_nums)]
    vert = process_arr(column_nums)
    to_return = hor + vert

    if len(to_return) == 1:
        return to_return[0]
    elif len(to_return) == 0:
        return 0
    return to_return

ans = 0

for grid in GRIDS:
    ans += process_grid(grid)

print(ans)
ans = 0

for grid in GRIDS:
    orig_ans = process_grid(grid)
    done = False
    for j in range(len(grid)):
        for k in range(len(grid[0])):
            if grid[j][k] == ".":
                grid[j][k] = "#"
            else:
                grid[j][k] = "."
            new_ans = process_grid(grid)
            if isinstance(new_ans, list) or new_ans != orig_ans and new_ans > 0:
                if isinstance(new_ans, list):
                    new_ans.remove(orig_ans)
                    ans += new_ans[0]
                else:
                    ans += new_ans
                done = True
                break
            if grid[j][k] == ".":
                grid[j][k] = "#"
            else:
                grid[j][k] = "."
        if done:
            break
print(ans)
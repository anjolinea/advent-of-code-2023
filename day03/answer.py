grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

def find_number(j, row):
    start = j
    end = j
    while start >= 0 and row[start].isdigit():
        start -= 1 
    if start < 0:
        start = 0
    elif not(row[start].isdigit()):
        start += 1
    
    while end < len(row) and row[end].isdigit():
        end += 1
    if end >= len(row):
        end = len(row) - 1
    elif not(row[end].isdigit()):
        end -= 1

    answer_to_return = int("".join(row[start:end+1]))
    return (answer_to_return, start, end)

def part_one():
    ans = 0 
    do_not_add_again = set()
    for i, row in enumerate(grid):
        for j, object in enumerate(row):
            if not(object.isdigit()) and object != ".":
                # object is a symbol
                for vert in [-1, 0, 1]:
                    for hor in [-1, 0, 1]:
                        if vert == 0 and hor == 0:
                            pass
                        if i + vert >= 0 and i + vert < len(grid) and j + hor >= 0 and j + hor < len(row):
                            if not((i+vert, j+hor) in do_not_add_again) and grid[i+vert][j+hor].isdigit():
                                num, start, end = find_number(j+hor, grid[i+vert])
                                for n in range(start, end+1):
                                    do_not_add_again.add((i+vert, n))
                                ans += num
    print(ans)

def part_two():
    ans = 0
    for i, row in enumerate(grid):
        for j, object in enumerate(row):
            if object == "*":
                # check if two adjacent numbers
                do_not_consider_again = set()
                nums_adj = 0
                prod = 1
                for vert in [-1, 0, 1]:
                    for hor in [-1, 0, 1]:
                        if vert == 0 and hor == 0:
                            pass
                        if i + vert >= 0 and i + vert < len(grid) and j + hor >= 0 and j + hor < len(row):
                            if not((i+vert, j+hor) in do_not_consider_again) and grid[i+vert][j+hor].isdigit():
                                num, start, end = find_number(j+hor, grid[i+vert])
                                for n in range(start, end+1):
                                    do_not_consider_again.add((i+vert, n))
                                nums_adj += 1
                                prod *= num
                if nums_adj == 2:
                    ans += prod
    print(ans)

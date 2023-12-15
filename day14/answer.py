grid = []

with open("input.txt", "r") as fhand:
    for line in fhand:
        grid.append(list(line.strip()))

def part_one():
    grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
    column_length = len(grid[0])
    ans = 0

    for column in grid:
        place = 0
        column_total = 0
        for i, obj in enumerate(column):
            if obj == "#":
                place = i + 1
            elif obj == "O":
                place += 1
                column_total += (column_length - place + 1)
        ans += column_total

    print(ans)  

def process_tilt(steps=4):
    global grid
    def process_column(column, column_length):
        new_column = ["."] * column_length
        place = 0
        for i, obj in enumerate(column):
            if obj == "#":
                place = i+1
                new_column[i] = "#"
            elif obj == "O":
                new_column[place] = "O"
                place += 1 

        return new_column
    
    def rotate_array(arr):
        return [[row[i] for row in arr] for i in range(len(arr[0]))]
    
    for i in range(steps):

        temp_grid = rotate_array(grid)
        column_length = len(temp_grid[0])
        if i % 4 == 2 or i % 4 == 3:
            new_grid = [process_column(column[::-1], column_length)[::-1] for column in temp_grid]
        else:
            new_grid = [process_column(column, column_length) for column in temp_grid]
        grid = new_grid

        # if i % 2 == 0:
        #     for row in rotate_array(new_grid):
        #         print("".join(row))

        #     print("\n")
        # else:
        #     for row in new_grid:
        #         print("".join(row))

        #     print("\n")

def get_score():
    global grid
    total = 0
    column_length = len(grid[0])
    for i, row in enumerate(grid):
        for obj in row:
            if obj == "O":
                total += column_length - i
    print(total)

process_tilt(steps=4000)
get_score()
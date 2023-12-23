grid = []
POSSIBLE_MOVES = [(-1,0), (1,0), (0,1), (0,-1)]

with open("input.txt") as fhand:
    for line in fhand:
        line = line.strip()
        grid.append(list(line))

MAX_X = len(grid)
MAX_Y = len(grid[0])

for i in range(MAX_X):
    for j in range(MAX_Y):
        if grid[i][j] == "S":
            start = (i,j)
            break

def process_plot(start, max_steps):
    plots = set([start])

    for _ in range(max_steps):
        new_plots = set()
        for plot in plots:
            x, y = plot
            for pos_move in POSSIBLE_MOVES:
                x1, y1 = pos_move
                if 0 <= x + x1 < MAX_X and 0 <= y + y1 < MAX_Y and grid[x+x1][y+y1] in [".", "S"]:
                    new_plots.add((x+x1, y+y1))
        plots = new_plots

    return len(plots)

def part_one():
    print(process_plot(start=start, max_steps=64))

def part_two():
    """
    Take advantage of the fact that input has straight lines to every border from S and the borders are all "."
    Also, by inspection, start is (65, 65) and the grid is 131 x 131. That means S is straight dab in the middle,
    65 spots away from any border. 

    A point is reachable in 26501365 steps if the number of steps to a point is reachable with any odd number of steps,
    where the odd number is <= 26501365. Thus, for any point, we find the optimal path to it and use a parity argument 
    to say it is reachable in 26501365 steps.
    """
    complete_odd = process_plot(start=start, max_steps=199) # 199 = random odd estimate for max points to get to any point (correct with higher estimates)
    complete_even = process_plot(start=start, max_steps=200)

    # pencils
    right_pencil = process_plot(start=(65,0), max_steps=130) # odd
    left_pencil = process_plot(start=(65,130), max_steps=130) # odd
    up_pencil = process_plot(start=(130,65), max_steps=130) # odd
    down_pencil = process_plot(start=(0,65), max_steps=130) # odd

    # right lower
    rl_missing_corner = process_plot(start=(0,0), max_steps=131+65-1) #196-3=193 
    rl_corner = process_plot(start=(0,0), max_steps=65-1) #

    # left lower
    ll_missing_corner = process_plot(start=(0,130), max_steps=131+65-1) 
    ll_corner = process_plot(start=(0,130), max_steps=65-1) 

    # right upper
    ru_missing_corner = process_plot(start=(130,0), max_steps=131+65-1) 
    ru_corner = process_plot(start=(130,0), max_steps=65-1) 

    # left upper
    lu_missing_corner = process_plot(start=(130,130), max_steps=131+65-1) 
    lu_corner = process_plot(start=(130,130), max_steps=65-1) 

    corner_weight = 202300 * (rl_corner + ll_corner + ru_corner + lu_corner)
    mc_weight = (202300-1) * (lu_missing_corner + rl_missing_corner + ru_missing_corner + ll_missing_corner)

    even_weight = ((202300 / 2) * (202300 / 2)) * complete_even * 4 # ok
    odd_weight = ((((202300 / 2) - 1) * (202300 / 2) * 4) + 1) * complete_odd

    ans = corner_weight + mc_weight + even_weight + odd_weight + right_pencil + left_pencil + up_pencil + down_pencil 
    print(int(ans))

part_two()
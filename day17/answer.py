from heapq import heappush, heappop
from math import inf

grid = []
with open("input.txt") as fhand:
    for line in fhand:
        line = line.strip()
        grid.append([int(c) for c in line])

def process_grid(min_move, max_move):
    heap = [(0, (0,0), "N")]
    heatloss_map = {(0,0): 0}
    visited = set()

    while len(heap) >= 1:
        heat_loss, coord, dir = heappop(heap)

        if coord[0] == len(grid)-1 and coord[1] == len(grid[0]) - 1:
            print(heat_loss)
            break

        if (coord, dir) not in visited:
            visited.add((coord, dir))

        # direction = neutral, R, L, U, D
        if dir == "N":
            poss_moves = [(1,0), (0,1)]
        elif dir in ["R", "L"]:
            poss_moves = [(1,0), (-1,0)]
        else:
            poss_moves = [(0,1), (0,-1)]

        for poss_move in poss_moves:
            new_heat_loss = heat_loss
            for steps in range(1, max_move + 1):
                poss_new_x = coord[0] + steps * poss_move[0]
                poss_new_y = coord[1] + steps * poss_move[1]
                if 0 <= poss_new_x < len(grid) and 0 <= poss_new_y < len(grid[0]): 
                    new_coord = (coord[0] + steps * poss_move[0], coord[1] + steps * poss_move[1])
                    new_heat_loss = new_heat_loss + grid[new_coord[1]][new_coord[0]]
                    if steps >= min_move:
                        if poss_move == (1,0):
                            new_dir = "D"
                        elif poss_move == (-1,0):
                            new_dir = "U"
                        elif poss_move == (0,1):
                            new_dir = "R"
                        else:
                            new_dir = "L"
                        new_node = (new_coord, new_dir)
                        if heatloss_map.get(new_node, inf) > new_heat_loss: 
                            heatloss_map[new_node] = new_heat_loss
                            heappush(heap, (new_heat_loss, new_coord, new_dir))

def part_one():
    process_grid(1,3)

def part_two():
    process_grid(4,10)

part_one()
part_two()
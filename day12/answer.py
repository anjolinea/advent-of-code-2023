from functools import cache

LINES = []

with open("input.txt") as f:
    for line in f:
        line = line.strip().split(" ")
        LINES.append((line[0], tuple([int(x) for x in line[1].split(",")])))

@cache
def process(code, nums, before="."):
    #print(code, nums, before)

    def process_dot():
        if before==".":
            return process(code[1:], nums, before=".")
        # else, # before it
        if nums[0] == 0:
            temp_nums = tuple(nums[1:])
            return process(code[1:], temp_nums, before=".")
        else:
            return 0
        
    def process_hash():
        if before==".":
            # start new number
            if len(nums) == 0:
                return 0
            # decrease first number
            temp_nums = tuple([x if i >= 1 else x-1 for i, x in enumerate(nums)])
            return process(code[1:], temp_nums, before="#")
        # else, # before it
        #print(code, nums)
        if nums[0] <= 0:
            return 0
        else:
            temp_nums = tuple([x if i >= 1 else x-1 for i, x in enumerate(nums)])
            return process(code[1:], temp_nums, before="#")
        
    
    if code == "":
        if len(nums) == 0 or nums == tuple([0]):
            return 1
        else:
            return 0
    
    char = code[0]
    if char == ".":
        return process_dot()
    elif char == "#":
        return process_hash()
    # char ?
    else:
        dot_answer = process_dot()
        hash_answer = process_hash()
        return dot_answer + hash_answer
    


def part_one():
    ans = 0
    for line in LINES:
        ans += process(line[0], line[1])
    print(ans)

def part_two():
    ans = 0
    for line in LINES:
        ans += process("?".join([line[0] for _ in range(0,5)]), line[1] * 5)
    print(ans)

part_two()
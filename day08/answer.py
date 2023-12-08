from math import lcm

MAPS = {}
PART_TWO_STARTS = set()
with open("input.txt") as f:
        instructions = []
        for line in f:
            if instructions == []:
                instructions = list(line.strip())
            elif line == "\n":
                pass
            else:
                temp = line.strip().split("=")
                MAPS[temp[0].strip()] = [x.strip() for x in temp[1].strip()[1:-1].split(",")]
                if temp[0].strip()[-1] == "A":
                    PART_TWO_STARTS.add(temp[0].strip())


def part_one():
    current = "AAA"
    ans = 0
    while current != "ZZZ":
        for instruction in instructions:
            if instruction == "L":
                current = MAPS[current][0]
            else:
                current = MAPS[current][1]
            ans += 1
            if current == "ZZZ":
                print(ans)
                break

# assumed separate end nodes and paths => cycle happens => lcm of the cycles
def part_two():
    def process(s):
        current = s
        ans = 0
        while current[-1] != "Z":
            for instruction in instructions:
                if instruction == "L":
                    current = MAPS[current][0]
                else:
                    current = MAPS[current][1]
                ans += 1
                if current[-1] == "Z":
                    return ans
                
    print(lcm(*[process(x) for x in PART_TWO_STARTS]))


part_two()
                
    
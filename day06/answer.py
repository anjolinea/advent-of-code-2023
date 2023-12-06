from math import sqrt, ceil, floor


def answer(TIME, DISTANCE):
    ans = 1
    for time, distance in list(zip(TIME, DISTANCE)):
        time = int(time)
        distance = int(distance)
        b = time
        a = -1
        c = -distance
        d = (b**2) - (4*a*c)  
    
        # find two solutions  
        sol1 = (-b-sqrt(d))/(2*a)  
        sol2 = (-b+sqrt(d))/(2*a)  

        num = floor(sol1) - ceil(sol2) + 1
        if sol1 == floor(sol1):
            num -= 1
        if sol2 == ceil(sol2):
            num -= 1
        ans *= num

    return ans

def part_one():
    with open("input.txt") as f:
        TIME = []
        DISTANCE = []
        for line in f:
            if TIME == []:
                TIME = list(filter(lambda x: x != '', line.strip().split(" ")[1:]))
            else:
                DISTANCE = list(filter(lambda x: x != '', line.strip().split(" ")[1:]))

    print(answer(TIME, DISTANCE))


def part_two():
    with open("input.txt") as f:
        TIME = []
        DISTANCE = []
        for line in f:
            if TIME == []:
                TIME = ["".join(line.strip().split(" ")[1:])]
            else:
                DISTANCE = ["".join(line.strip().split(" ")[1:])]

    print(answer(TIME, DISTANCE))

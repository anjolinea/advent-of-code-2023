def part_one():

    def parse_string(s):
        s_half = s.split(":")
        game_id = int(s_half[0].split(" ")[1])
        
        subgames = s_half[1].split(";")

        for sg in subgames:
            colours = sg.split(",")
            for c in colours:
                d = c.split(" ")
                num = int(d[1])
                colour = d[2]
                if colour == "red" and num > 12:
                    return 0
                elif colour == "blue" and num > 14:
                    return 0
                elif colour == "green" and num > 13:
                    return 0
        return game_id
    
    ans = 0
    with open("input.txt") as f:
        for line in f:
            ans += parse_string(line.strip())

    print(ans)


def part_two():

    def parse_string(s):
        s_half = s.split(":")
        subgames = s_half[1].split(";")

        max_red = 0
        max_blue = 0
        max_green = 0

        for sg in subgames:
            colours = sg.split(",")
            for c in colours:
                d = c.split(" ")
                num = int(d[1])
                colour = d[2]
                if colour == "red" and num > max_red:
                    max_red = num
                elif colour == "blue" and num > max_blue:
                    max_blue = num
                elif colour == "green" and num > max_green:
                    max_green = num
        return max_red * max_blue * max_green


    ans = 0
    with open("input.txt") as f:
        for line in f:
            ans += parse_string(line.strip())

    print(ans)
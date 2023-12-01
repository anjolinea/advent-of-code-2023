def part_one():
    ans = 0

    def get_first_digit(s):
        for c in s:
            if c.isdigit():
                return int(c)

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            tens = get_first_digit(line)
            ones = get_first_digit(line[::-1])
            ans += tens * 10 + ones

    print(ans)


def part_two():
    WRITTEN_NUMBERS =  dict(zip(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], list(range(1,10))))
    ans = 0

    def get_first_digit(s):
        for i, c in enumerate(s):
            if c.isdigit():
                return i, int(c)
            
    def get_tens_number(s):
        lowest_index = len(s)
        lowest_index_number = None

        for wn in WRITTEN_NUMBERS:
            index = s.find(wn)
            if index != -1 and index < lowest_index:
                lowest_index = index
                lowest_index_number = WRITTEN_NUMBERS[wn]

        int_i, int_d = get_first_digit(s)
        if int_i < lowest_index:
            return int_d
        else:
            return lowest_index_number
        

    def get_ones_number(s):
        modified_written_numbers = dict(zip([wn[::-1] for wn in WRITTEN_NUMBERS.keys()], list(range(1,10))))
        lowest_index = len(s)
        lowest_index_number = None

        for wn in modified_written_numbers:
            index = s.find(wn)
            if index != -1 and index < lowest_index:
                lowest_index = index
                lowest_index_number = modified_written_numbers[wn]

        int_i, int_d = get_first_digit(s)
        if int_i < lowest_index:
            return int_d
        else:
            return lowest_index_number
        
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            tens = get_tens_number(line)
            ones = get_ones_number(line[::-1])
            ans += tens * 10 + ones

    print(ans)

part_two()
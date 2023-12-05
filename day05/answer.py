def part_one():
    MAPS = {}
    with open("input.txt") as f:
        prepare_new_section = True
        seed_line = True
        for line in f:
            if line == '\n':
                prepare_new_section = True
            elif seed_line:
                SEEDS = list(map(int, line.strip().split(" ")[1:]))
                seed_line = False
            elif prepare_new_section:
                new_section = line.strip().split(" ")[0]
                MAPS[new_section] = []
                prepare_new_section = False
            else:
                MAPS[new_section].append(tuple(list(map(int, line.strip().split(" ")))))

    def process_step(source_val, maps):
        for dest, source, range_length in maps:
            if source <= source_val and source_val < source + range_length:
                diff = source_val - source
                return dest + diff
        return source_val
            
    def process_seed(seed):
        return_val = seed
        for v in MAPS.values():
            return_val = process_step(return_val, v)
        return return_val
    print(min([process_seed(s) for s in SEEDS]))

def part_two():
    MAPS = {}
    with open("input.txt") as f:
        prepare_new_section = True
        seed_line = True
        for line in f:
            if line == '\n':
                prepare_new_section = True
            elif seed_line:
                temp = list(map(int, line.strip().split(" ")[1:]))
                SEEDS = list(zip([temp[i] for i in range(len(temp)) if i % 2 == 0], [temp[i] for i in range(len(temp)) if i % 2 == 1]))
                seed_line = False
            elif prepare_new_section:
                new_section = line.strip().split(" ")[0]
                MAPS[new_section] = []
                prepare_new_section = False
            else:
                MAPS[new_section].append(tuple(list(map(int, line.strip().split(" ")))))

    def process_range(start, start_len, maps):
        RANGES = []
        DONE = []
        for dest, source, range_length in maps:
            # intersecition of [source, source + range_length] and [start, start + start_len]
            if start < source + range_length and source < start + start_len:
                range_start = max(start, source)
                range_end = min(source + range_length, start + start_len)
                RANGES.append((range_start + dest - source, range_end - range_start))
                DONE.append((range_start, range_end - range_start))
        DONE.sort()
        current_start = start
        for s, e in DONE:
            if current_start < s:
                RANGES.append((current_start, s - current_start))
            current_start = s + e
        if current_start < start + start_len:
            RANGES.append((current_start, start + start_len - current_start))
        return RANGES
    
    def process():
        CURRENT_RANGES = [tuple(x) for x in SEEDS]
        NEXT_RANGES = []
        for k, m in MAPS.items():
            for cr, crl in CURRENT_RANGES:
                NEXT_RANGES += process_range(cr, crl,m)
            CURRENT_RANGES = NEXT_RANGES
            NEXT_RANGES = []

        CURRENT_RANGES.sort()
        return CURRENT_RANGES

    print(process()[0][0])

part_two()
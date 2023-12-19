from collections import deque
import copy

parts = []
rules = dict()

with open("input.txt") as fhand:
    is_part = False

    for line in fhand:
        if line == "\n":
            is_part = True
            continue
        line = line.strip()
        if is_part:
            part_dict = dict([(x[0], int(x[2:])) for x in line[1:-1].split(",")])
            parts.append(part_dict)
        else:
            line = line[:-1].split("{")
            key = line[0]
            wf = []
            for x in line[1].split(","):
                if ":" in x:
                    str_rule, next_rule = tuple(x.split(":"))
                    if ">" in str_rule:
                        letter, number = tuple(str_rule.split(">"))
                        wf.append((letter, ">", int(number), next_rule))
                    else:
                        letter, number = tuple(str_rule.split("<"))
                        wf.append((letter, "<", int(number), next_rule))
                else:
                    last_rule = x
            rules[key] = (wf, last_rule)

def part_one():
    ans = 0
    for part in parts:
        current_rule = "in"
        while current_rule not in ["A", "R"]:
            reached_end = False
            wf, last_rule = rules[current_rule]
            for r in wf:
                letter, comp, num, next_rule = r
                if comp == "<" and part[letter] < num:
                    current_rule = next_rule
                    reached_end = True
                    break
                elif comp == ">" and part[letter] > num:
                    current_rule = next_rule
                    reached_end = True
                    break
            if not reached_end:
                current_rule = last_rule

        if current_rule == "A":
            ans += sum(part.values())

    print(ans)

def part_two():
    init_range = dict(zip(["x", "m", "a", "s"], [[1,4000] for _ in range(4)]))
    queue = deque([("in", init_range)])
    acceptable_ranges = []
    not_acceptable_ranges = []

    while queue:
        rule_name, rule_range = queue.popleft()
        wf, last_rule = rules[rule_name]
        current_rule_range = copy.deepcopy(rule_range)
        for r in wf:
            letter, comp, num, next_rule = r
            new_rule_range = copy.deepcopy(current_rule_range)
            if comp == "<":
                true_num = min(new_rule_range[letter][1], num-1)
                new_rule_range[letter][1] = true_num
                current_rule_range[letter][0] = true_num+1
            elif comp == ">":
                true_num = max(new_rule_range[letter][0], num+1)
                new_rule_range[letter][0] = true_num
                current_rule_range[letter][1] = true_num-1

            if next_rule not in ["A", "R"]:
                queue.append((next_rule, new_rule_range))
            elif next_rule == "A":
                acceptable_ranges.append(new_rule_range)

        last_range = copy.deepcopy(current_rule_range)
        if last_rule not in ["A", "R"]:
            queue.append((last_rule, last_range))
        elif last_rule == "A":
            acceptable_ranges.append(last_range)
        

    #print(acceptable_ranges)

    ans = 0
    for ar in acceptable_ranges:
        to_add = 1
        for k, v in ar.items():
            to_add *= (v[1] - v[0] + 1)
        ans += to_add
    print(ans)



LINES = []

with open("input.txt") as f:
    for line in f:
        LINES.append([int(x) for x in line.strip().split(" ")])

def part_one():
    def process(row):
        if [x for x in row if x == 0] == row:
            return 0
        differences = [row[i]-row[i-1]for i in range(1,len(row))]
        add_on = process(differences)
        return row[-1]+add_on

    ans = 0
    for line in LINES:
        ans += process(line)

    print(ans)

def part_two():
    def process(row):
        if [x for x in row if x == 0] == row:
            return 0
        differences = [row[i]-row[i-1]for i in range(1,len(row))]
        diff = process(differences)
        return row[0]-diff

    ans = 0
    for line in LINES:
        ans += process(line)

    print(ans)

part_two()
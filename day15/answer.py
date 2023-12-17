LINES = []

with open("input.txt") as f:
    line = f.readline()
    line = line.strip().split(",")

def hash_algo(current_value, letter):
    # x * 17 mod 256
    return (((current_value + ord(letter)) * 17) % 256)

def part_one():
    def process_instruction(instruction):
        current_value = 0
        for c in instruction:
            current_value = hash_algo(current_value, c)
        return current_value

    ans = 0
    for instruction in line:
        ans += process_instruction(instruction)

    print(ans)

def part_two():
    boxes = [dict() for _ in range(256)]
    def process_instruction(instruction):
        if "=" in instruction:
            operation, focal_length = instruction.split("=")
            current_value = 0
            for c in operation:
                current_value = hash_algo(current_value, c)

            boxes[current_value][operation] = focal_length
        else:
            operation = instruction[:-1]
            current_value = 0
            for c in operation:
                current_value = hash_algo(current_value, c)

            if operation in boxes[current_value]:
                del boxes[current_value][operation]

    for instruction in line:
        process_instruction(instruction)
    
    ans = 0
    for i, box in enumerate(boxes):
        for j, (key, value) in enumerate(box.items()):
            ans += (i+1) * (j+1) * int(value)
    print(ans)

    


part_two()
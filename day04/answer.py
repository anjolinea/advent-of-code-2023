ans = 0

def part_one():
    def process_line(s):
        winning, mine = tuple(s.split("|"))
        winning = set([item for item in winning.split(":")[1].split(" ") if item != ""])
        mine = set([item for item in mine.split(" ") if item != ""])
        num_of_winning = len(mine.intersection(winning))
        return 0 if num_of_winning == 0 else 2 ** (num_of_winning - 1)
        
    with open("input.txt") as f:
        for line in f:
            ans += process_line(line.strip())

    print(ans)

def part_two():
    def process_line(s):
        winning, mine = tuple(s.split("|"))
        winning = set([item for item in winning.split(":")[1].split(" ") if item != ""])
        mine = set([item for item in mine.split(" ") if item != ""])
        num_of_winning = len(mine.intersection(winning))
        return num_of_winning
        
    NUM_OF_CARDS = {}
    
    with open("input.txt") as f:
        card_number = 1
        for line in f:
            NUM_OF_CARDS[card_number] = NUM_OF_CARDS.get(card_number, 1)
            num_of_winning = process_line(line.strip())
            for i in range(1, num_of_winning+1):
                NUM_OF_CARDS[card_number+i] = NUM_OF_CARDS.get(card_number+i, 1)
                NUM_OF_CARDS[card_number+i] += NUM_OF_CARDS[card_number]
            card_number += 1
    
    print(sum(NUM_OF_CARDS.values()))

part_two()
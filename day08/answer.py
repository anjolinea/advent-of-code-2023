from collections import Counter

def part_one():
    HANDS = []

    with open("input.txt") as f:
        for line in f:
            temp = line.strip().split(" ")
            HANDS.append((temp[0], temp[1]))

    def get_kind(hand):
        counter = dict(Counter(list(hand)))
        vals = counter.values()
        if 5 in vals:
            return 6
        elif 4 in vals:
            return 5
        elif 3 in vals and 2 in vals:
            return 4
        elif 3 in vals:
            return 3
        elif len([x for x in vals if x == 2]) == 2:
            return 2
        elif 2 in vals:
            return 1
        else:
            return 0
        
    RANK_WITH_HANDS = {}
    for hand, bid in HANDS:
        t = get_kind(hand)
        RANK_WITH_HANDS[t] = RANK_WITH_HANDS.get(t, [])
        RANK_WITH_HANDS[t].append((hand, int(bid)))

    rank = len(HANDS)
    ans = 0
    alphabet = "AKQJT98765432"
    for loh in [x[1] for x in sorted(RANK_WITH_HANDS.items(), reverse=True)]:
        loh = sorted(loh, key=lambda word: [alphabet.index(c) for c in word[0]])
        for hand, bid in loh:
            ans += rank * bid
            rank -= 1

    print(ans)


def part_two():
    HANDS = []

    with open("input.txt") as f:
        for line in f:
            temp = line.strip().split(" ")
            HANDS.append((temp[0], temp[1]))

    def get_kind(hand):
        counter = dict(Counter(list(hand)))
        vals = counter.values()
        if 5 in vals:
            return 6
        elif 4 in vals:
            if "J" in counter:
                return 6
            return 5
        elif 3 in vals and 2 in vals:
            # JJJXX or XXXJJ
            if "J" in counter:
                return 6
            return 4
        elif 3 in vals:
            # JJJXY or XXXJY => four of a kind
            if "J" in counter:
                return 5
            return 3
        elif len([x for x in vals if x == 2]) == 2:
            # XXYYJ or JJXXY
            if counter.get("J", 0) == 1:
                return 4
            elif counter.get("J", 0) == 2:
                return 5
            return 2
        elif 2 in vals:
            # JJXYZ or XXYZJ
            if "J" in counter:
                return 3
            return 1
        else:
            # JXYZP
            if "J" in counter:
                return 1
            return 0
        
    RANK_WITH_HANDS = {}
    for hand, bid in HANDS:
        t = get_kind(hand)
        RANK_WITH_HANDS[t] = RANK_WITH_HANDS.get(t, [])
        RANK_WITH_HANDS[t].append((hand, int(bid)))

    rank = len(HANDS)
    ans = 0
    alphabet = "AKQT98765432J"
    for loh in [x[1] for x in sorted(RANK_WITH_HANDS.items(), reverse=True)]:
        loh = sorted(loh, key=lambda word: [alphabet.index(c) for c in word[0]])
        for hand, bid in loh:
            ans += rank * bid
            rank -= 1

    print(ans)



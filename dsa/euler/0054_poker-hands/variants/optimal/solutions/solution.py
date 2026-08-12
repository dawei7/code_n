VAL_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


def hand_rank(hand: list[str]) -> tuple:
    vals = sorted([VAL_MAP[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    is_flush = len(set(suits)) == 1
    is_straight = len(set(vals)) == 5 and (vals[0] - vals[4] == 4)

    if vals == [14, 5, 4, 3, 2]:
        is_straight = True
        vals = [5, 4, 3, 2, 1]

    counts = sorted([(vals.count(v), v) for v in set(vals)], key=lambda x: (x[0], x[1]), reverse=True)

    if is_straight and is_flush:
        return (8, vals)
    if counts[0][0] == 4:
        return (7, counts[0][1], counts[1][1])
    if counts[0][0] == 3 and counts[1][0] == 2:
        return (6, counts[0][1], counts[1][1])
    if is_flush:
        return (5, vals)
    if is_straight:
        return (4, vals)
    if counts[0][0] == 3:
        return (3, counts[0][1], [x[1] for x in counts[1:]])
    if counts[0][0] == 2 and counts[1][0] == 2:
        return (2, counts[0][1], counts[1][1], counts[2][1])
    if counts[0][0] == 2:
        return (1, counts[0][1], [x[1] for x in counts[1:]])
    return (0, vals)


def solve() -> int:
    """How many hands does Player 1 win in poker.txt?
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    import urllib.request
    url = "https://projecteuler.net/resources/documents/0054_poker.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip().split() for line in text.strip().splitlines() if line.strip()]
    
    p1_wins = 0
    for line in lines:
        p1_hand = line[:5]
        p2_hand = line[5:]
        if hand_rank(p1_hand) > hand_rank(p2_hand):
            p1_wins += 1

    return p1_wins

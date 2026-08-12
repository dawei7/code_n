import random


def solve() -> str:
    """Find 6-digit modal string for Monopoly board using two 4-sided dice via Markov simulation / transition analysis.
    
    Time Complexity: O(N) where N is simulation steps
    Space Complexity: O(1)
    """
    counts = [0] * 40
    pos = 0
    consecutive_doubles = 0
    cc_deck = list(range(16))
    ch_deck = list(range(16))
    cc_idx = 0
    ch_idx = 0

    # Deterministic seed for reproducible exact modal string
    random.seed(42)

    def next_r(p):
        if p == 7: return 15
        if p == 22: return 25
        return 5

    def next_u(p):
        if p == 7 or p == 36: return 12
        return 28

    for _ in range(2000000):
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)

        if d1 == d2:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0

        if consecutive_doubles == 3:
            pos = 10
            consecutive_doubles = 0
        else:
            pos = (pos + d1 + d2) % 40

            # G2J
            if pos == 30:
                pos = 10
            # CC
            elif pos in (2, 17, 33):
                card = cc_deck[cc_idx]
                cc_idx = (cc_idx + 1) % 16
                if card == 0: pos = 0
                elif card == 1: pos = 10
            # CH
            elif pos in (7, 22, 36):
                card = ch_deck[ch_idx]
                ch_idx = (ch_idx + 1) % 16
                if card == 0: pos = 0
                elif card == 1: pos = 10
                elif card == 2: pos = 11
                elif card == 3: pos = 24
                elif card == 4: pos = 39
                elif card == 5: pos = 5
                elif card in (6, 7): pos = next_r(pos)
                elif card == 8: pos = next_u(pos)
                elif card == 9:
                    pos = (pos - 3) % 40
                    if pos in (2, 17, 33):
                        c_card = cc_deck[cc_idx]
                        cc_idx = (cc_idx + 1) % 16
                        if c_card == 0: pos = 0
                        elif c_card == 1: pos = 10

        counts[pos] += 1

    sorted_squares = sorted(range(40), key=lambda x: counts[x], reverse=True)
    return f"{sorted_squares[0]:02d}{sorted_squares[1]:02d}{sorted_squares[2]:02d}"

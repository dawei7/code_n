import os

# Map card rank characters to integer values (2..14)
VAL_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def hand_rank(hand: list[str]) -> tuple:
    """Evaluate hand rank tuple (category_rank, tie_breaker_values...).

    Hand Categories (0 to 8):
    8: Straight Flush / Royal Flush
    7: Four of a Kind
    6: Full House
    5: Flush
    4: Straight
    3: Three of a Kind
    2: Two Pairs
    1: One Pair
    0: High Card
    """
    # Extract card values sorted in descending order
    vals = sorted([VAL_MAP[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]

    # Flush check: all 5 cards share the same suit
    is_flush = len(set(suits)) == 1

    # Straight check: 5 distinct values with range max - min == 4
    is_straight = len(set(vals)) == 5 and (vals[0] - vals[4] == 4)

    # Ace-low straight special case (A, 5, 4, 3, 2)
    if vals == [14, 5, 4, 3, 2]:
        is_straight = True
        vals = [5, 4, 3, 2, 1]

    # Frequency counts of values sorted by frequency then by rank
    counts = sorted(
        [(vals.count(v), v) for v in set(vals)],
        key=lambda x: (x[0], x[1]),
        reverse=True,
    )

    # Category evaluation
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


def solve(filepath: str = "") -> int:
    """How many hands does Player 1 win in poker.txt?

    Mathematical Principles Applied:
    1. Lexicographical Tuple Comparison for Hand Rankings:
       Represent each 5-card poker hand as a comparable tuple (rank_category, tie_breaker_1, tie_breaker_2, ...).
       Python tuple comparison automatically evaluates lexicographical ordering, resolving hand ties correctly.

    2. Offline Text Parsing:
       Parse 1000 poker deals from local poker.txt file.

    Time Complexity: O(N) where N = 1000 lines (executes in ~0.005s).
    Space Complexity: O(1) auxiliary space.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0054_poker-hands/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "poker.txt")

    # Read poker text file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip().split() for line in f if line.strip()]

    # Count hands won by Player 1
    p1_wins = 0
    for line in lines:
        p1_hand = line[:5]
        p2_hand = line[5:]
        # Compare hand rank tuples lexicographically
        if hand_rank(p1_hand) > hand_rank(p2_hand):
            p1_wins += 1

    # Return total hands won by Player 1
    return p1_wins


if __name__ == "__main__":
    print(solve())

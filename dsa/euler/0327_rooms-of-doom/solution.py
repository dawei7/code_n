"""Project Euler 327: Rooms of Doom

Find sum_{C=3}^{40} M(C, 30), where M(C, R) is the minimum number of cards
required to travel through R rooms carrying up to C cards at any time.
"""

from __future__ import annotations


def m_card_requirement(c: int, r: int) -> int:
    """Calculates M(C, R) using backward induction on the Jeep/Desert supply recurrence."""
    x = 1  # 1 card required to open the final exit door
    for _ in range(r):
        if x <= c - 1:
            x = x + 1
        else:
            # Round trips to deliver surplus cards: each round trip delivers (C - 2) cards and consumes 2 cards
            k = (x - 2) // (c - 2)
            x = x + 1 + 2 * k
    return x


def solve(min_c: int = 3, max_c: int = 40, num_rooms: int = 30) -> str:
    """Calculates sum_{C=min_c}^{max_c} M(C, num_rooms) via backward dynamic programming."""
    total_cards = 0
    for c in range(min_c, max_c + 1):
        total_cards += m_card_requirement(c, num_rooms)

    return str(total_cards)


if __name__ == "__main__":
    print(solve())

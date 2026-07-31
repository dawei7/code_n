from collections import Counter


def solve(cards: list[str], x: str) -> int:
    first = Counter()
    second = Counter()
    centers = 0

    for card in cards:
        if card[0] == x and card[1] == x:
            centers += 1
        elif card[0] == x:
            first[card[1]] += 1
        elif card[1] == x:
            second[card[0]] += 1

    first_total = sum(first.values())
    second_total = sum(second.values())
    first_largest = max(first.values(), default=0)
    second_largest = max(second.values(), default=0)

    def side_score(total: int, largest: int, allocated: int) -> int:
        combined = total + allocated
        return min(combined // 2, combined - max(largest, allocated))

    return max(
        side_score(first_total, first_largest, allocated)
        + side_score(
            second_total,
            second_largest,
            centers - allocated,
        )
        for allocated in range(centers + 1)
    )

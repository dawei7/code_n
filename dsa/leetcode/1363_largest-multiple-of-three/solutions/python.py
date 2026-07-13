"""Optimal solution for LeetCode 1363: Largest Multiple of Three."""


def solve(digits: list[int]) -> str:
    counts = [0] * 10
    total = 0
    for digit in digits:
        counts[digit] += 1
        total += digit

    def remove_one(remainder: int) -> bool:
        for digit in range(remainder, 10, 3):
            if counts[digit]:
                counts[digit] -= 1
                return True
        return False

    def remove_two(remainder: int) -> bool:
        removed: list[int] = []
        for digit in range(remainder, 10, 3):
            while counts[digit] and len(removed) < 2:
                counts[digit] -= 1
                removed.append(digit)
            if len(removed) == 2:
                return True
        for digit in removed:
            counts[digit] += 1
        return False

    remainder = total % 3
    if remainder == 1:
        if not remove_one(1):
            remove_two(2)
    elif remainder == 2:
        if not remove_one(2):
            remove_two(1)

    answer = "".join(str(digit) * counts[digit] for digit in range(9, -1, -1))
    if not answer:
        return ""
    return "0" if answer[0] == "0" else answer

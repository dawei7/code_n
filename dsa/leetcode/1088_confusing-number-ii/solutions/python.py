"""Optimal solution for LeetCode 1088: Confusing Number II."""


def solve(n: int) -> int:
    rotations = ((0, 0), (1, 1), (6, 9), (8, 8), (9, 6))
    answer = 0

    def generate(value: int, rotated: int, place: int) -> None:
        nonlocal answer
        for digit, mapped in rotations:
            if value == 0 and digit == 0:
                continue
            candidate = value * 10 + digit
            if candidate > n:
                break
            rotated_candidate = mapped * place + rotated
            if candidate != rotated_candidate:
                answer += 1
            generate(candidate, rotated_candidate, place * 10)

    generate(0, 0, 1)
    return answer

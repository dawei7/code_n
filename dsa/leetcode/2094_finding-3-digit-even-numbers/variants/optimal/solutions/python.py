from collections import Counter


def solve(digits: list[int]) -> list[int]:
    available = Counter(digits)
    answer = []

    for number in range(100, 1000, 2):
        required = Counter(map(int, str(number)))
        if all(required[digit] <= available[digit] for digit in required):
            answer.append(number)

    return answer

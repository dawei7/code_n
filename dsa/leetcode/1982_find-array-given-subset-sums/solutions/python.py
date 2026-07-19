from collections import Counter


def solve(n: int, sums: list[int]) -> list[int]:
    current = sorted(sums)
    answer = []

    for _ in range(n):
        magnitude = current[1] - current[0]
        remaining = Counter(current)
        without = []
        with_value = []

        for total in current:
            if remaining[total] == 0:
                continue
            without.append(total)
            with_value.append(total + magnitude)
            remaining[total] -= 1
            remaining[total + magnitude] -= 1

        if 0 in without:
            answer.append(magnitude)
            current = without
        else:
            answer.append(-magnitude)
            current = with_value

    return answer

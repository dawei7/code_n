from collections import Counter


def solve(nums: list[int]) -> int:
    counts = Counter(nums)
    ones = counts.get(1, 0)
    answer = ones if ones % 2 else max(0, ones - 1)

    for start in counts:
        if start == 1:
            continue

        current = start
        length = 0
        while counts.get(current, 0) >= 2:
            length += 2
            current *= current

        if counts.get(current, 0) >= 1:
            length += 1
        else:
            length -= 1

        answer = max(answer, length)

    return answer

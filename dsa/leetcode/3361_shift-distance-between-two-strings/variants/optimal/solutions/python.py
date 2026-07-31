def solve(s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
    next_prefix = [0] * 27
    previous_prefix = [0] * 27

    for i in range(26):
        next_prefix[i + 1] = next_prefix[i] + nextCost[i]
        previous_prefix[i + 1] = previous_prefix[i] + previousCost[i]

    answer = 0
    for source, target in zip(s, t):
        start = ord(source) - ord("a")
        end = ord(target) - ord("a")

        if end >= start:
            forward = next_prefix[end] - next_prefix[start]
        else:
            forward = next_prefix[26] - next_prefix[start] + next_prefix[end]

        if end <= start:
            backward = previous_prefix[start + 1] - previous_prefix[end + 1]
        else:
            backward = (
                previous_prefix[start + 1]
                + previous_prefix[26]
                - previous_prefix[end + 1]
            )

        answer += min(forward, backward)

    return answer

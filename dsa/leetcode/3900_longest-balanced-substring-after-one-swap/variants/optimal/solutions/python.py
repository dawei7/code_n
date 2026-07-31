from collections import defaultdict, deque


def solve(s: str) -> int:
    zero_count = s.count("0")
    one_count = len(s) - zero_count
    maximum_candidate_length = 2 * min(zero_count, one_count)

    positions: dict[int, deque[int]] = defaultdict(deque)
    positions[0].append(0)
    score = 0
    answer = 0

    for end in range(1, len(s) + 1):
        score += 1 if s[end - 1] == "1" else -1
        earliest_allowed = end - maximum_candidate_length

        for starting_score in (score, score - 2, score + 2):
            starts = positions.get(starting_score)
            if starts is None:
                continue
            while starts and starts[0] < earliest_allowed:
                starts.popleft()
            if starts:
                answer = max(answer, end - starts[0])

        positions[score].append(end)

    return answer

def solve(queries: list[list[int]]) -> int:
    def prefix_steps(upto: int) -> int:
        total = 0
        start = 1
        steps = 1
        while start <= upto:
            next_start = start * 4
            total += (min(upto + 1, next_start) - start) * steps
            start = next_start
            steps += 1
        return total

    answer = 0
    for left, right in queries:
        required = prefix_steps(right) - prefix_steps(left - 1)
        answer += (required + 1) // 2
    return answer

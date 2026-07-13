def _steps_sum(upto: int) -> int:
    if upto <= 0:
        return 0
    total = 0
    start = 1
    steps = 1
    while start <= upto:
        end = min(upto, start * 4 - 1)
        total += (end - start + 1) * steps
        start *= 4
        steps += 1
    return total


def solve(queries: list[list[int]]) -> int:
    answer = 0
    for left, right in queries:
        required = _steps_sum(right) - _steps_sum(left - 1)
        answer += (required + 1) // 2
    return answer

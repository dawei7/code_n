def solve(rungs: list[int], dist: int) -> int:
    answer = 0
    previous = 0

    for rung in rungs:
        answer += (rung - previous - 1) // dist
        previous = rung

    return answer

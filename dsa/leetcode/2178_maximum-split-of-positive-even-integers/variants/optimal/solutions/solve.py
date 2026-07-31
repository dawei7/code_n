def solve(finalSum: int) -> list[int]:
    if finalSum % 2:
        return []

    answer = []
    next_even = 2
    while finalSum >= next_even:
        answer.append(next_even)
        finalSum -= next_even
        next_even += 2

    answer[-1] += finalSum
    return answer

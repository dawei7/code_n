def solve(bulbs: list[int], k: int) -> int:
    days = [0] * len(bulbs)
    for day, position in enumerate(bulbs, 1):
        days[position - 1] = day

    answer = len(bulbs) + 1
    left = 0
    right = k + 1
    index = 1

    while right < len(days):
        if days[index] < days[left] or days[index] <= days[right]:
            if index == right:
                answer = min(answer, max(days[left], days[right]))
            left = index
            right = left + k + 1
        index += 1

    return -1 if answer > len(bulbs) else answer


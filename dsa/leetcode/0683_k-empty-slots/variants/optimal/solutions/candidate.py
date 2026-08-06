def solve(bulbs: list[int], k: int) -> int:
    days = [0] * len(bulbs)
    for day, position in enumerate(bulbs, 1):
        days[position - 1] = day

    answer = len(bulbs) + 1
    left = 0
    right = k + 1
    scan_position = 1

    while right < len(days):
        if days[scan_position] < days[left] or days[scan_position] <= days[right]:
            if scan_position == right:
                answer = min(answer, max(days[left], days[right]))
            left = scan_position
            right = left + k + 1
        scan_position += 1

    return -1 if answer > len(bulbs) else answer

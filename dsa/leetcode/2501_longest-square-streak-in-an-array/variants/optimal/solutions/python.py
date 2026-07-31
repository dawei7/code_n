def solve(nums):
    values = set(nums)
    answer = -1

    for start in values:
        length = 0
        current = start
        while current in values:
            length += 1
            current *= current
        if length >= 2:
            answer = max(answer, length)

    return answer

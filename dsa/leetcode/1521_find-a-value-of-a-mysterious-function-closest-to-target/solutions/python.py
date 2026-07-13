def solve(arr, target):
    current = set()
    answer = float("inf")
    for value in arr:
        current = {value & previous for previous in current}
        current.add(value)
        for candidate in current:
            answer = min(answer, abs(candidate - target))
    return int(answer if answer != float("inf") else 0)

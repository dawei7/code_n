def solve(capacity: list[int]) -> int:
    prefix = [0]
    for value in capacity:
        prefix.append(prefix[-1] + value)

    eligible = {}
    result = 0
    for right in range(2, len(capacity)):
        left = right - 2
        key = (capacity[left], prefix[left] + 2 * capacity[left])
        eligible[key] = eligible.get(key, 0) + 1
        result += eligible.get((capacity[right], prefix[right]), 0)

    return result

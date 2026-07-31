def solve(s: str, queries: list[list[int]]) -> list[list[int]]:
    locations: dict[int, list[int]] = {}
    n = len(s)

    for left in range(n):
        if s[left] == "0":
            if 0 not in locations:
                locations[0] = [left, left]
            continue

        value = 0
        for right in range(left, min(left + 30, n)):
            value = (value << 1) | int(s[right])
            if value not in locations:
                locations[value] = [left, right]

    return [locations.get(first ^ second, [-1, -1]) for first, second in queries]

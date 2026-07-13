def solve(s: str, c: str) -> list[int]:
    length = len(s)
    distances = [length] * length

    previous = -length
    for index, character in enumerate(s):
        if character == c:
            previous = index
        distances[index] = index - previous

    following = 2 * length
    for index in range(length - 1, -1, -1):
        if s[index] == c:
            following = index
        distances[index] = min(distances[index], following - index)

    return distances

def solve(
    n: int,
    nums: list[int],
    maxDiff: int,
    queries: list[list[int]],
) -> list[int]:
    order = sorted(range(n), key=lambda node: nums[node])
    values = [nums[node] for node in order]
    position = [0] * n

    for index, node in enumerate(order):
        position[node] = index

    farthest = [0] * n
    right = 0

    for left in range(n):
        if right < left:
            right = left
        while right + 1 < n and values[right + 1] - values[left] <= maxDiff:
            right += 1
        farthest[left] = right

    jumps = [farthest]
    for _ in range(1, n.bit_length()):
        previous = jumps[-1]
        jumps.append([previous[previous[index]] for index in range(n)])

    answer: list[int] = []
    for source, target in queries:
        left, right = sorted((position[source], position[target]))

        if left == right:
            answer.append(0)
            continue

        current = left
        distance = 0

        for power in range(len(jumps) - 1, -1, -1):
            next_position = jumps[power][current]
            if current < next_position < right:
                current = next_position
                distance += 1 << power

        if jumps[0][current] >= right:
            answer.append(distance + 1)
        else:
            answer.append(-1)

    return answer

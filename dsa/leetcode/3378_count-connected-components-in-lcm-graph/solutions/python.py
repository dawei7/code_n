def solve(nums: list[int], threshold: int) -> int:
    parent = list(range(threshold + 1))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(a: int, b: int) -> None:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    representative = [0] * (threshold + 1)

    for value in nums:
        if value > threshold:
            continue
        for multiple in range(value, threshold + 1, value):
            if representative[multiple] == 0:
                representative[multiple] = value
            else:
                union(value, representative[multiple])

    components = sum(1 for value in nums if value > threshold)
    roots = {find(value) for value in nums if value <= threshold}
    return components + len(roots)

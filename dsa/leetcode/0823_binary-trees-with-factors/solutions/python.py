MODULUS = 1_000_000_007


def solve(arr: list[int]) -> int:
    values = sorted(arr)
    ways: dict[int, int] = {}
    total = 0

    for index, root in enumerate(values):
        root_ways = 1
        for factor_index in range(index):
            left = values[factor_index]
            if root % left != 0:
                continue
            right = root // left
            if right in ways:
                root_ways += ways[left] * ways[right]

        ways[root] = root_ways % MODULUS
        total = (total + ways[root]) % MODULUS

    return total

def solve(instructions: list[int]) -> int:
    modulus = 1_000_000_007
    maximum = max(instructions)
    tree = [0] * (maximum + 1)

    def prefix_sum(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    def add(index: int) -> None:
        while index <= maximum:
            tree[index] += 1
            index += index & -index

    cost = 0
    for inserted, value in enumerate(instructions):
        less = prefix_sum(value - 1)
        greater = inserted - prefix_sum(value)
        cost += min(less, greater)
        add(value)

    return cost % modulus

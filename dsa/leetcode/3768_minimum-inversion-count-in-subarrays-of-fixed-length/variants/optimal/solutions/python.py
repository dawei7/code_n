class FenwickTree:
    def __init__(self, size: int) -> None:
        self.nodes = [0] * (size + 1)

    def update(self, position: int, difference: int) -> None:
        while position < len(self.nodes):
            self.nodes[position] += difference
            position += position & -position

    def query(self, position: int) -> int:
        result = 0
        while position > 0:
            result += self.nodes[position]
            position -= position & -position
        return result


def solve(nums: list[int], k: int) -> int:
    ranks = {value: index + 1 for index, value in enumerate(sorted(set(nums)))}
    frequencies = FenwickTree(len(ranks))

    current = 0
    for inserted, value in enumerate(nums[:k]):
        value_rank = ranks[value]
        current += inserted - frequencies.query(value_rank)
        frequencies.update(value_rank, 1)

    best = current
    for left, value in enumerate(nums[k:]):
        removed_rank = ranks[nums[left]]
        current -= frequencies.query(removed_rank - 1)
        frequencies.update(removed_rank, -1)

        added_rank = ranks[value]
        current += k - 1 - frequencies.query(added_rank)
        frequencies.update(added_rank, 1)
        if current < best:
            best = current

    return best

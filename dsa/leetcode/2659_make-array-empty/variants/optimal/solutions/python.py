class FenwickTree:
    def __init__(self, size):
        # The tree array is 1-indexed, so size+1 elements are needed.
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        # index is 1-based
        while index <= self.size:
            self.tree[index] += delta
            # Move to the next index to update (parent in the implicit tree structure)
            index += index & (-index)

    def query(self, index):
        # index is 1-based
        s = 0
        while index > 0:
            s += self.tree[index]
            # Move to the previous index to query (parent in the implicit tree structure)
            index -= index & (-index)
        return s

def solve(nums: list[int]) -> int:
    n = len(nums)

    # Remove values in increasing order. Between removals, count how many
    # still-alive elements are rotated past in circular order.
    indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])
    ft = FenwickTree(n)
    for i in range(1, n + 1):
        ft.update(i, 1)

    total_cost = 0
    current_index = 0

    for _, original_index in indexed_nums:
        if original_index >= current_index:
            rotations = ft.query(original_index) - ft.query(current_index)
        else:
            rotations = (ft.query(n) - ft.query(current_index)) + ft.query(original_index)

        total_cost += rotations + 1
        ft.update(original_index + 1, -1)
        current_index = original_index

    return total_cost

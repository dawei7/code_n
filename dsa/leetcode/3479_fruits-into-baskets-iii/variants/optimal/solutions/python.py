def solve(fruits: list[int], baskets: list[int]) -> int:
    n = len(baskets)
    # Segment tree to store the maximum capacity in a range
    tree = [-1] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = baskets[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

    def query(node, start, end, fruit_size):
        # If the max in this range is less than fruit_size, no basket here
        if tree[node] < fruit_size:
            return -1
        if start == end:
            return start

        mid = (start + end) // 2
        # Try left child first to find the smallest index
        res = query(2 * node, start, mid, fruit_size)
        if res == -1:
            res = query(2 * node + 1, mid + 1, end, fruit_size)
        return res

    build(1, 0, n - 1)

    placed = 0
    for fruit in fruits:
        idx = query(1, 0, n - 1, fruit)
        if idx != -1:
            placed += 1
            update(1, 0, n - 1, idx, -1)

    return n - placed

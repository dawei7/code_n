def solve(nums: list[int], k: int) -> int:
    # The maximum value in nums is 10^5 based on problem constraints
    MAX_VAL = 100000
    # Segment tree size: 4 * MAX_VAL is sufficient
    tree = [0] * (4 * (MAX_VAL + 1))

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

    def query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return max(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r))

    max_len = 0
    for x in nums:
        # Query the range [max(1, x-k), x-1]
        prev_max = query(1, 1, MAX_VAL, max(1, x - k), x - 1)
        current_len = prev_max + 1
        update(1, 1, MAX_VAL, x, current_len)
        max_len = max(max_len, current_len)

    return max_len

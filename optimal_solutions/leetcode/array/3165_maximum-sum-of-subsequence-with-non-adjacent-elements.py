def solve(nums, queries):
    MOD = 10**9 + 7
    n = len(nums)
    
    # Each node stores: (v00, v01, v10, v11)
    # v00: max sum excluding both ends
    # v01: max sum excluding start, including end
    # v10: max sum including start, excluding end
    # v11: max sum including both ends
    tree = [(0, 0, 0, 0)] * (4 * n)

    def merge(left, right):
        l00, l01, l10, l11 = left
        r00, r01, r10, r11 = right
        
        return (
            max(l00 + r10, l01 + r00),
            max(l00 + r11, l01 + r01),
            max(l10 + r10, l11 + r00),
            max(l10 + r11, l11 + r01)
        )

    def build(node, start, end):
        if start == end:
            val = max(0, nums[start])
            tree[node] = (0, 0, 0, val)
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    def update(node, start, end, idx, val):
        if start == end:
            v = max(0, val)
            tree[node] = (0, 0, 0, v)
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    build(1, 0, n - 1)
    
    total_sum = 0
    for idx, val in queries:
        update(1, 0, n - 1, idx, val)
        res = tree[1]
        total_sum = (total_sum + max(res)) % MOD
        
    return total_sum

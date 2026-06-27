def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # Segment tree stores:
    # sum_sq: sum of squares of distinct counts for subarrays ending at current index
    # sum_val: sum of distinct counts for subarrays ending at current index
    # lazy: lazy propagation value for incrementing distinct counts
    sum_sq = [0] * (4 * n)
    sum_val = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def push_up(node):
        sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
        sum_val[node] = (sum_val[2 * node] + sum_val[2 * node + 1]) % MOD

    def apply(node, start, end, val):
        # (x+v)^2 = x^2 + 2xv + v^2
        # sum((x+v)^2) = sum(x^2) + 2v*sum(x) + v^2 * count
        count = end - start + 1
        sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val * count) % MOD
        sum_val[node] = (sum_val[node] + val * count) % MOD
        lazy[node] += val

    def push_down(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            apply(2 * node, start, mid, lazy[node])
            apply(2 * node + 1, mid + 1, end, lazy[node])
            lazy[node] = 0

    def update(node, start, end, l, r, val):
        if l <= start and end <= r:
            apply(node, start, end, val)
            return
        push_down(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            update(2 * node, start, mid, l, r, val)
        if r > mid:
            update(2 * node + 1, mid + 1, end, l, r, val)
        push_up(node)

    last_seen = {}
    total_sum = 0
    current_sum_sq = 0
    
    for i, x in enumerate(nums):
        prev = last_seen.get(x, -1)
        # Update range (prev, i]
        update(1, 0, n - 1, prev + 1, i, 1)
        last_seen[x] = i
        # sum_sq[1] now holds the sum of squares of distinct counts for all subarrays ending at i
        total_sum = (total_sum + sum_sq[1]) % MOD
        
    return total_sum

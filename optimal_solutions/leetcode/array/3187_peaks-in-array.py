def solve(nums, queries):
    n = len(nums)
    bit = [0] * (n + 1)

    def update_bit(i, delta):
        i += 1
        while i <= n:
            bit[i] += delta
            i += i & (-i)

    def query_bit(i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    def is_peak(i):
        if 0 < i < n - 1:
            return 1 if nums[i - 1] < nums[i] > nums[i + 1] else 0
        return 0

    # Initialize BIT
    for i in range(1, n - 1):
        if is_peak(i):
            update_bit(i, 1)

    results = []
    for q in queries:
        if q[0] == 1:
            l, r = q[1], q[2]
            # Peaks must be strictly inside [l, r], so range is [l+1, r-1]
            if l + 1 > r - 1:
                results.append(0)
            else:
                results.append(query_bit(r - 1) - query_bit(l))
        else:
            idx, val = q[1], q[2]
            # Before update, remove peak status of affected indices
            for i in range(idx - 1, idx + 2):
                if is_peak(i):
                    update_bit(i, -1)
            
            nums[idx] = val
            
            # After update, add peak status of affected indices
            for i in range(idx - 1, idx + 2):
                if is_peak(i):
                    update_bit(i, 1)
                    
    return results

import math

def solve(nums1, nums2, queries):
    n = len(nums1)
    # tree stores the count of 1s in the range
    tree = [0] * (4 * n)
    lazy = [False] * (4 * n)
    
    # Precompute sum of nums2 for each index to handle weighted sum
    # We only need the sum of nums2 where nums1[i] is 1.
    # Since nums2 is static, we can use a Fenwick tree or prefix sums for nums2.
    prefix_sum2 = [0] * (n + 1)
    for i in range(n):
        prefix_sum2[i+1] = prefix_sum2[i] + nums2[i]
        
    def build(node, start, end):
        if start == end:
            tree[node] = nums1[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]
        
    def push(node, start, end):
        if lazy[node]:
            mid = (start + end) // 2
            tree[2 * node] = (mid - start + 1) - tree[2 * node]
            lazy[2 * node] = not lazy[2 * node]
            tree[2 * node + 1] = (end - mid) - tree[2 * node + 1]
            lazy[2 * node + 1] = not lazy[2 * node + 1]
            lazy[node] = False
            
    def update(node, start, end, l, r):
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            tree[node] = (end - start + 1) - tree[node]
            lazy[node] = not lazy[node]
            return
        push(node, start, end)
        mid = (start + end) // 2
        update(2 * node, start, mid, l, r)
        update(2 * node + 1, mid + 1, end, l, r)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    # To calculate sum(nums1[i] * nums2[i]), we need the indices where nums1[i] == 1.
    # A segment tree can track the sum of nums2[i] where nums1[i] == 1.
    # Let's redefine the tree to store sum of nums2[i] for active indices.
    tree_sum2 = [0] * (4 * n)
    
    def build_sum(node, start, end):
        if start == end:
            tree_sum2[node] = nums2[start] if nums1[start] == 1 else 0
            return
        mid = (start + end) // 2
        build_sum(2 * node, start, mid)
        build_sum(2 * node + 1, mid + 1, end)
        tree_sum2[node] = tree_sum2[2 * node] + tree_sum2[2 * node + 1]
        
    # We need the total sum of nums2 in a range to perform the flip:
    # new_sum = total_sum_in_range - old_sum_in_range
    range_sum2 = [0] * (4 * n)
    def build_range_sum2(node, start, end):
        if start == end:
            range_sum2[node] = nums2[start]
            return
        mid = (start + end) // 2
        build_range_sum2(2 * node, start, mid)
        build_range_sum2(2 * node + 1, mid + 1, end)
        range_sum2[node] = range_sum2[2 * node] + range_sum2[2 * node + 1]

    build_sum(1, 0, n - 1)
    build_range_sum2(1, 0, n - 1)
    
    def update_sum(node, start, end, l, r):
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            tree_sum2[node] = range_sum2[node] - tree_sum2[node]
            lazy[node] = not lazy[node]
            return
        push_sum(node, start, end)
        mid = (start + end) // 2
        update_sum(2 * node, start, mid, l, r)
        update_sum(2 * node + 1, mid + 1, end, l, r)
        tree_sum2[node] = tree_sum2[2 * node] + tree_sum2[2 * node + 1]
        
    def push_sum(node, start, end):
        if lazy[node]:
            mid = (start + end) // 2
            tree_sum2[2 * node] = range_sum2[2 * node] - tree_sum2[2 * node]
            lazy[2 * node] = not lazy[2 * node]
            tree_sum2[2 * node + 1] = range_sum2[2 * node + 1] - tree_sum2[2 * node + 1]
            lazy[2 * node + 1] = not lazy[2 * node + 1]
            lazy[node] = False

    results = []
    for q in queries:
        if q[0] == 1:
            update_sum(1, 0, n - 1, q[1], q[2])
        elif q[0] == 3:
            results.append(tree_sum2[1])
    return results

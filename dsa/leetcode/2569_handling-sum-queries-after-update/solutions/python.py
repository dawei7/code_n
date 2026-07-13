def solve(nums1, nums2, queries):
    n = len(nums1)
    tree = [0] * (4 * n)
    lazy = [False] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = nums1[start]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def push(node, start, end):
        if not lazy[node] or start == end:
            return
        mid = (start + end) // 2
        left = 2 * node
        right = left + 1
        tree[left] = (mid - start + 1) - tree[left]
        lazy[left] = not lazy[left]
        tree[right] = (end - mid) - tree[right]
        lazy[right] = not lazy[right]
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

    build(1, 0, n - 1)
    total = sum(nums2)
    results = []
    for q in queries:
        if q[0] == 1:
            update(1, 0, n - 1, q[1], q[2])
        elif q[0] == 2:
            total += q[1] * tree[1]
        elif q[0] == 3:
            results.append(total)
    return results

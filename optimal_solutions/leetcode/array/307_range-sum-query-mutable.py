def solve(arr, n, queries, q):
    # Segment Tree implementation using a flat array
    tree = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            arr[idx] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        p1 = query(2 * node, start, mid, l, r)
        p2 = query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2

    if n > 0:
        build(1, 0, n - 1)
    
    results = []
    for op in queries:
        if op[0] == 'update':
            update(1, 0, n - 1, op[1], op[2])
        elif op[0] == 'sum':
            results.append(query(1, 0, n - 1, op[1], op[2]))
            
    return results

def solve(nums: list[int], queries: list[list[int]]) -> int:
    mod = 10**9 + 7
    n = len(nums)
    tree = [(0, 0, 0, 0)] * (4 * n)

    def merge(left, right):
        l00, l01, l10, l11 = left
        r00, r01, r10, r11 = right
        return (
            max(l00 + r10, l01 + r00),
            max(l00 + r11, l01 + r01),
            max(l10 + r10, l11 + r00),
            max(l10 + r11, l11 + r01),
        )

    def build(node, low, high):
        if low == high:
            tree[node] = (0, 0, 0, max(0, nums[low]))
            return
        mid = (low + high) // 2
        build(node * 2, low, mid)
        build(node * 2 + 1, mid + 1, high)
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

    def update(node, low, high, index, value):
        if low == high:
            tree[node] = (0, 0, 0, max(0, value))
            return
        mid = (low + high) // 2
        if index <= mid:
            update(node * 2, low, mid, index, value)
        else:
            update(node * 2 + 1, mid + 1, high, index, value)
        tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

    build(1, 0, n - 1)
    answer = 0
    for index, value in queries:
        update(1, 0, n - 1, index, value)
        answer = (answer + tree[1][3]) % mod

    return answer

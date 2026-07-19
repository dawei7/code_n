class SegmentTree:
    def __init__(self, active: list[int]):
        self.size = 1
        while self.size < len(active):
            self.size *= 2
        self.tree = [-1] * (2 * self.size)
        for index, value in enumerate(active):
            self.tree[self.size + index] = index if value else -1
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def set(self, index: int, enabled: bool) -> None:
        node = self.size + index
        self.tree[node] = index if enabled else -1
        node //= 2
        while node:
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
            node //= 2

    def max_active(self) -> int:
        return self.tree[1]


def solve(words: list[str], k: int) -> list[int]:
    if len(words) - 1 < k:
        return [0] * len(words)

    children: list[dict[str, int]] = [{}]
    counts = [0]
    depths = [0]

    for word in words:
        node = 0
        for char in word:
            nxt = children[node].get(char)
            if nxt is None:
                nxt = len(children)
                children[node][char] = nxt
                children.append({})
                counts.append(0)
                depths.append(depths[node] + 1)
            node = nxt
            counts[node] += 1

    max_depth = max(depths, default=0)
    valid_by_depth = [0] * (max_depth + 1)
    for node in range(1, len(counts)):
        if counts[node] >= k:
            valid_by_depth[depths[node]] += 1

    active = [1 if count else 0 for count in valid_by_depth]
    tree = SegmentTree(active)
    answer: list[int] = []

    for word in words:
        node = 0
        disabled: list[int] = []
        seen_depths: set[int] = set()
        for char in word:
            node = children[node][char]
            depth = depths[node]
            if (
                counts[node] == k
                and valid_by_depth[depth] == 1
                and depth not in seen_depths
            ):
                tree.set(depth, False)
                disabled.append(depth)
                seen_depths.add(depth)
        answer.append(max(0, tree.max_active()))
        for depth in disabled:
            tree.set(depth, True)

    return answer

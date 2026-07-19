class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class _Node:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key: int):
        self.key = key
        z = (key + 0x9E3779B97F4A7C15) & ((1 << 64) - 1)
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & ((1 << 64) - 1)
        self.priority = z ^ (z >> 31)
        self.left = None
        self.right = None


def _merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.priority < right.priority:
        left.right = _merge(left.right, right)
        return left
    right.left = _merge(left, right.left)
    return right


def _split(root, key: int):
    if root is None:
        return None, None
    if root.key < key:
        left, right = _split(root.right, key)
        root.right = left
        return root, right
    left, right = _split(root.left, key)
    root.left = right
    return left, root


def _insert(root, key: int):
    left, right = _split(root, key)
    return _merge(_merge(left, _Node(key)), right)


def _erase(root, key: int):
    if root is None:
        return None
    if key == root.key:
        return _merge(root.left, root.right)
    if key < root.key:
        root.left = _erase(root.left, key)
    else:
        root.right = _erase(root.right, key)
    return root


def _contains(root, key: int) -> bool:
    while root is not None:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False


def _predecessor(root, key: int):
    result = None
    while root is not None:
        if root.key < key:
            result = root.key
            root = root.right
        else:
            root = root.left
    return result


def _successor(root, key: int):
    result = None
    while root is not None:
        if root.key > key:
            result = root.key
            root = root.left
        else:
            root = root.right
    return result


def _minimum(root):
    while root.left is not None:
        root = root.left
    return root.key


def _maximum(root):
    while root.right is not None:
        root = root.right
    return root.key


def solve(colors, queries):
    n = len(colors)
    if n == 0:
        return []

    count_by_len = FenwickTree(n)
    sum_by_len = FenwickTree(n)
    root = None
    break_count = 0

    def dist(left: int, right: int) -> int:
        return (right - left) % n or n

    def add_len(length: int, delta: int) -> None:
        count_by_len.add(length, delta)
        sum_by_len.add(length, delta * length)

    def add_break(pos: int) -> None:
        nonlocal root, break_count
        if _contains(root, pos):
            return
        if break_count == 0:
            add_len(n, 1)
        else:
            prev_pos = _predecessor(root, pos)
            next_pos = _successor(root, pos)
            if prev_pos is None:
                prev_pos = _maximum(root)
            if next_pos is None:
                next_pos = _minimum(root)
            add_len(dist(prev_pos, next_pos), -1)
            add_len(dist(prev_pos, pos), 1)
            add_len(dist(pos, next_pos), 1)
        root = _insert(root, pos)
        break_count += 1

    def remove_break(pos: int) -> None:
        nonlocal root, break_count
        if not _contains(root, pos):
            return
        if break_count == 1:
            add_len(n, -1)
        else:
            prev_pos = _predecessor(root, pos)
            next_pos = _successor(root, pos)
            if prev_pos is None:
                prev_pos = _maximum(root)
            if next_pos is None:
                next_pos = _minimum(root)
            add_len(dist(prev_pos, pos), -1)
            add_len(dist(pos, next_pos), -1)
            add_len(dist(prev_pos, next_pos), 1)
        root = _erase(root, pos)
        break_count -= 1

    def is_break(pos: int) -> bool:
        return colors[pos] == colors[(pos + 1) % n]

    for i in range(n):
        if is_break(i):
            add_break(i)

    results = []
    for query in queries:
        if query[0] == 1:
            size = query[1]
            if size <= 1:
                results.append(n)
            elif size > n:
                results.append(0)
            elif break_count == 0:
                results.append(n)
            else:
                below_count = count_by_len.sum(size - 1)
                below_sum = sum_by_len.sum(size - 1)
                usable_count = break_count - below_count
                usable_sum = n - below_sum
                results.append(usable_sum - (size - 1) * usable_count)
        else:
            index, color = query[1], query[2]
            if colors[index] == color:
                continue
            affected = ((index - 1) % n, index)
            for pos in affected:
                if is_break(pos):
                    remove_break(pos)
            colors[index] = color
            for pos in affected:
                if is_break(pos):
                    add_break(pos)

    return results

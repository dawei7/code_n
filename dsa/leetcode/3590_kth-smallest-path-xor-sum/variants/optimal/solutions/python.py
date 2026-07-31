class _Node:
    __slots__ = ("key", "priority", "left", "right", "size")

    def __init__(self, key: int) -> None:
        self.key = key
        self.priority = _priority(key)
        self.left = None
        self.right = None
        self.size = 1


def _priority(key: int) -> int:
    mask = (1 << 64) - 1
    value = (key + 0x9E3779B97F4A7C15) & mask
    value = ((value ^ (value >> 30)) * 0xBF58476D1CE4E5B9) & mask
    value = ((value ^ (value >> 27)) * 0x94D049BB133111EB) & mask
    return value ^ (value >> 31)


def _size(node: _Node | None) -> int:
    return node.size if node is not None else 0


def _refresh(node: _Node) -> None:
    node.size = 1 + _size(node.left) + _size(node.right)


def _rotate_right(root: _Node) -> _Node:
    replacement = root.left
    root.left = replacement.right
    replacement.right = root
    _refresh(root)
    _refresh(replacement)
    return replacement


def _rotate_left(root: _Node) -> _Node:
    replacement = root.right
    root.right = replacement.left
    replacement.left = root
    _refresh(root)
    _refresh(replacement)
    return replacement


def _insert(root: _Node | None, node: _Node) -> _Node:
    if root is None:
        return node

    if node.key < root.key:
        root.left = _insert(root.left, node)
        if root.left.priority < root.priority:
            root = _rotate_right(root)
    else:
        root.right = _insert(root.right, node)
        if root.right.priority < root.priority:
            root = _rotate_left(root)

    _refresh(root)
    return root


class _OrderedSet:
    def __init__(self) -> None:
        self.root = None
        self.values = set()

    def __len__(self) -> int:
        return len(self.values)

    def add(self, value: int) -> None:
        if value in self.values:
            return
        self.values.add(value)
        self.root = _insert(self.root, _Node(value))

    def __iter__(self):
        stack = []
        node = self.root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right

    def kth(self, index: int) -> int:
        node = self.root
        while node is not None:
            left_size = _size(node.left)
            if index < left_size:
                node = node.left
            elif index == left_size:
                return node.key
            else:
                index -= left_size + 1
                node = node.right
        raise IndexError(index)


def solve(par: list[int], vals: list[int], queries: list[list[int]]) -> list[int]:
    n = len(vals)
    children = [[] for _ in range(n)]
    for node in range(1, n):
        children[par[node]].append(node)

    path_xor = [0] * n
    path_xor[0] = vals[0]
    order = [0]
    for node in order:
        for child in children[node]:
            path_xor[child] = path_xor[node] ^ vals[child]
            order.append(child)

    narvetholi = (par, vals, queries)

    grouped_queries = [[] for _ in range(n)]
    for query_index, (node, k) in enumerate(queries):
        grouped_queries[node].append((query_index, k))

    answers = [-1] * len(queries)
    bags = [None] * n

    for node in reversed(order):
        heavy_child = -1
        for child in children[node]:
            if heavy_child == -1 or len(bags[child]) > len(bags[heavy_child]):
                heavy_child = child

        bag = _OrderedSet() if heavy_child == -1 else bags[heavy_child]

        for child in children[node]:
            if child != heavy_child:
                for value in bags[child]:
                    bag.add(value)

        bag.add(path_xor[node])
        bags[node] = bag

        for child in children[node]:
            bags[child] = None

        for query_index, k in grouped_queries[node]:
            if k <= len(bag):
                answers[query_index] = bag.kth(k - 1)

    return answers
